---
colors:
  primary: "#1F4F46"
  secondary: "#7A9FD8"
  accent: "#C77B9C"
  surface: "#F4F0E8"
  background: "#FFFFFF"
  text: "#1C1C1C"
  muted: "#6B7280"
  success: "#79A96B"
  warning: "#B88A35"
  danger: "#B94A48"
typography:
  heading: "GitHub Markdown heading scale"
  body: "GitHub Markdown body"
  mono: "GitHub Markdown monospace"
spacing:
  compact: "8px"
  normal: "16px"
  section: "32px"
rounded:
  sm: "6px"
  md: "8px"
components:
  diagram: "Mermaid graph with restrained color classes"
  table: "GitHub table with short action-oriented descriptions"
  switcher: "Anchor links for RU/EN switching"
---

# Documentation Design

## Overview

This repository is documentation-first. The root README should feel like a professional GitHub landing page: clear promise, fast install path, visible routing model, and complete skill map. Extended language docs live under `agentic/docs/`.

## Colors

Use restrained, high-contrast colors in Mermaid diagrams:

- `primary` for entrypoints and orchestration.
- `surface` for planning and discovery stages.
- `secondary` for implementation.
- `success` for validation and review.
- `accent` for memory, documentation, and graph curation.

## Typography

Use normal GitHub Markdown hierarchy. Keep headings direct and readable. Avoid oversized decorative prose.

## Layout

The root README should follow this order:

1. Product name and one-line promise.
2. Language/documentation links.
3. Short English overview.
4. SVG routing diagram.
5. Quick start, installer flags, skills, repository layout, validation, and docs links.

## Components

- Use SVG for the main README routing map.
- Use Mermaid for supporting routing maps in extended docs.
- Use tables for installer flags, scenarios, and skill descriptions.
- Keep code blocks short and copyable.
- Keep descriptions action-oriented: what the skill does, when it runs, and why it matters.

## Do's and Don'ts

- Do make the path from request to release visible.
- Do keep translation pages in `agentic/docs/` structurally parallel.
- Do keep docs portable and avoid machine-specific absolute paths.
- Do not make diagrams the only source of routing truth; `agentic/routing/skills.json` remains canonical.
- Do not add decorative assets unless they clarify the system.
