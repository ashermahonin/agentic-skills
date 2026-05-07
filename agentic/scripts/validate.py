#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAME_RE = re.compile(r"^[a-z0-9-]+$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
STALE_RESEARCH_DOC = "research" + "-alignment"

def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)

def check_skill(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing frontmatter", errors)
        return
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"{path}: malformed frontmatter", errors)
        return
    fm = parts[1]
    name = None
    desc = None
    for line in fm.splitlines():
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip()
    if not name or not NAME_RE.match(name):
        fail(f"{path}: invalid name", errors)
    if not desc or len(desc) < 80:
        fail(f"{path}: description too short", errors)
    if path.parent.name != name:
        fail(f"{path}: folder/name mismatch", errors)
    if not (path.parent / "agents" / "openai.yaml").exists():
        fail(f"{path}: missing agents/openai.yaml", errors)
    for heading in ["## Role", "## Start By", "## Procedure", "## Output Artifacts", "## Quality Bar", "## Handoff", "## References"]:
        if heading not in text:
            fail(f"{path}: missing {heading}", errors)
    if "TODO" in text:
        fail(f"{path}: contains TODO", errors)
    ref_match = re.search(r"`references/([^`]+)`", text)
    if not ref_match:
        fail(f"{path}: missing reference link", errors)
    elif not (path.parent / "references" / ref_match.group(1)).exists():
        fail(f"{path}: referenced file does not exist: {ref_match.group(1)}", errors)
    openai = path.parent / "agents" / "openai.yaml"
    if openai.exists() and f"Use ${path.parent.name}" not in openai.read_text(encoding="utf-8"):
        fail(f"{openai}: default_prompt must mention ${path.parent.name}", errors)

def check_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        raw = match.group(1).strip()
        if not raw or raw.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = raw.split("#", 1)[0]
        if not target:
            continue
        target_path = (path.parent / target).resolve()
        try:
            target_path.relative_to(ROOT)
        except ValueError:
            fail(f"{path}: link escapes repository: {raw}", errors)
            continue
        if not target_path.exists():
            fail(f"{path}: broken link: {raw}", errors)

def check_svg(path: Path, errors: list[str]) -> None:
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        fail(f"{path}: invalid SVG XML: {exc}", errors)

def main() -> int:
    errors: list[str] = []
    for required_root in ["README.md", "DESIGN.md", "AGENTS.md", "CLAUDE.md", "install.sh"]:
        if not (ROOT / required_root).exists():
            fail(f"missing {required_root}", errors)
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
    for token in ["agentic/docs/README.ru.md", "agentic/docs/README.es.md", "agentic/docs/README.zh.md", "agentic/docs/assets/routing-flow.svg", "--global", "--local", "CODEX_HOME", "CLAUDE_HOME", "AGENTS_HOME", "## Overview"]:
        if token not in readme:
            fail(f"README.md missing {token}", errors)
    for doc in ["README.md", "README.ru.md", "README.es.md", "README.zh.md", "research-summary.md", "assets/routing-flow.svg", "assets/routing-flow.ru.svg", "assets/routing-flow.es.svg", "assets/routing-flow.zh.svg"]:
        if not (ROOT / "agentic" / "docs" / doc).exists():
            fail(f"missing agentic/docs/{doc}", errors)
    markdown_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for md in markdown_files:
        if md.exists():
            check_markdown_links(md, errors)
            if STALE_RESEARCH_DOC in md.read_text(encoding="utf-8"):
                fail(f"{md}: stale removed research link", errors)
    for svg in (ROOT / "agentic" / "docs" / "assets").glob("*.svg"):
        check_svg(svg, errors)
    routing_readme = ROOT / "agentic" / "routing" / "README.md"
    if routing_readme.exists():
        routing_text = routing_readme.read_text(encoding="utf-8")
        for token in ["## Русский", "## English", "```mermaid"]:
            if token not in routing_text:
                fail(f"routing/README.md missing {token}", errors)
    skills_dir = ROOT / "agentic" / "skills"
    skill_files = sorted(skills_dir.glob("*/SKILL.md"))
    if len(skill_files) != 14:
        fail(f"expected 14 skills, found {len(skill_files)}", errors)
    for skill in skill_files:
        check_skill(skill, errors)
    routing = json.loads((ROOT / "agentic" / "routing" / "skills.json").read_text(encoding="utf-8"))
    routed = {item["name"] for item in routing.get("skills", [])}
    actual = {p.parent.name for p in skill_files}
    if routed != actual:
        fail(f"routing mismatch: {sorted(actual ^ routed)}", errors)
    for entrypoint, sequence in routing.get("entrypoints", {}).items():
        for skill in sequence:
            if skill not in actual:
                fail(f"entrypoint {entrypoint}: unknown skill {skill}", errors)
        if "service-implementation" in sequence and "qa-eval" in sequence:
            if sequence.index("qa-eval") < sequence.index("service-implementation"):
                fail(f"entrypoint {entrypoint}: qa-eval appears before service-implementation", errors)
        if "decompose-work" in sequence and "service-implementation" in sequence:
            if sequence.index("service-implementation") < sequence.index("decompose-work"):
                fail(f"entrypoint {entrypoint}: service-implementation appears before decompose-work", errors)
    if "service-implementation" in routing.get("permissions", {}).get("read_only", []):
        fail("service-implementation must not be read_only", errors)
    if "service-implementation" not in routing.get("permissions", {}).get("write_after_gates", []):
        fail("service-implementation must be write_after_gates", errors)
    skeleton = ROOT / "agentic" / "obsidian" / "project-skeleton"
    for required in ["00-home.md", "14-system-context.md", "28-parallelization-plan.md", "85-migration-plan.md"]:
        if not (skeleton / required).exists():
            fail(f"missing skeleton {required}", errors)
    for note in skeleton.rglob("*.md"):
        if "[[]]" in note.read_text(encoding="utf-8"):
            fail(f"{note}: empty wikilink placeholder", errors)
    installer = ROOT / "install.sh"
    if not installer.exists():
        fail("missing install.sh", errors)
    elif not os.access(installer, os.X_OK):
        fail("install.sh is not executable", errors)
    else:
        installer_text = installer.read_text(encoding="utf-8")
        for token in ["CODEX_HOME", "CLAUDE_HOME", "AGENTS_HOME", "DRY_RUN"]:
            if token not in installer_text:
                fail(f"install.sh missing {token}", errors)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"valid: {len(skill_files)} expanded skills, GitHub docs, routing, Obsidian skeleton, and installer")
    return 0

if __name__ == "__main__":
    sys.exit(main())
