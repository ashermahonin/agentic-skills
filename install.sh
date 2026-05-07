#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
SKILLS_DIR="$SCRIPT_DIR/agentic/skills"

TARGET="all"
MODE="global"
PROJECT_DIR=""
FORCE=0
COPY=0
DRY_RUN=0
LIST_ONLY=0
RESOLVED_HOME=""
DEST_DIR=""

usage() {
  cat <<'USAGE'
Usage:
  ./install.sh --global [--target codex|claude|agents|all] [--copy] [--force] [--dry-run]
  ./install.sh --local /path/to/project [--target codex|claude|agents|all] [--copy] [--force] [--dry-run]
  ./install.sh --list

Modes:
  --global              Install into user-level skill folders.
  --local PATH          Install into one project: PATH/.codex/skills, PATH/.claude/skills, PATH/.agents/skills.

Targets:
  --target codex        Install only for Codex.
  --target claude       Install only for Claude Code.
  --target agents       Install only for generic .agents.
  --target all          Install for all targets. Default.

Options:
  --copy                Copy skill folders instead of symlinking them.
  --force               Replace existing real directories. Symlinks are always refreshed safely.
  --dry-run             Print actions without changing files.
  --list                List available skills and exit.
  -h, --help            Show this help.

Environment:
  CODEX_HOME            Codex home for --global. Default: $HOME/.codex
  CLAUDE_HOME           Claude Code home for --global. Default: $HOME/.claude
  AGENTS_HOME           Generic agents home for --global. Default: $HOME/.agents
USAGE
}

die() {
  printf '%s\n' "$*" >&2
  exit 1
}

list_skills() {
  for skill_dir in "$SKILLS_DIR"/*; do
    [ -d "$skill_dir" ] || continue
    [ -f "$skill_dir/SKILL.md" ] || continue
    basename "$skill_dir"
  done
}

resolve_home() {
  var_name="$1"
  default_suffix="$2"
  eval "value=\${$var_name:-}"
  if [ -n "$value" ]; then
    RESOLVED_HOME="$value"
    return
  fi
  if [ -z "${HOME:-}" ]; then
    die "$var_name is not set and HOME is unavailable; set $var_name or HOME"
  fi
  RESOLVED_HOME="$HOME/$default_suffix"
}

set_target_dir() {
  host="$1"
  base="$2"
  case "$MODE:$host" in
    global:codex) resolve_home CODEX_HOME .codex; DEST_DIR="$RESOLVED_HOME/skills" ;;
    global:claude) resolve_home CLAUDE_HOME .claude; DEST_DIR="$RESOLVED_HOME/skills" ;;
    global:agents) resolve_home AGENTS_HOME .agents; DEST_DIR="$RESOLVED_HOME/skills" ;;
    local:codex) DEST_DIR="$base/.codex/skills" ;;
    local:claude) DEST_DIR="$base/.claude/skills" ;;
    local:agents) DEST_DIR="$base/.agents/skills" ;;
    *) die "unknown target: $host" ;;
  esac
}

install_one_skill() {
  skill_dir="$1"
  dest_dir="$2"
  name=$(basename "$skill_dir")
  dest="$dest_dir/$name"

  if [ "$DRY_RUN" -eq 1 ]; then
    if [ "$COPY" -eq 1 ]; then
      printf 'copy %s -> %s\n' "$skill_dir" "$dest"
    else
      printf 'link %s -> %s\n' "$skill_dir" "$dest"
    fi
    return
  fi

  mkdir -p "$dest_dir"

  if [ -L "$dest" ]; then
    rm "$dest"
  elif [ -e "$dest" ]; then
    if [ "$FORCE" -ne 1 ]; then
      die "$dest exists and is not a symlink; rerun with --force to replace it"
    fi
    rm -rf "$dest"
  fi

  if [ "$COPY" -eq 1 ]; then
    cp -R "$skill_dir" "$dest"
  else
    ln -s "$skill_dir" "$dest"
  fi
}

install_target() {
  host="$1"
  base="$2"
  set_target_dir "$host" "$base"
  dest_dir="$DEST_DIR"
  printf 'Installing %s skills into %s\n' "$host" "$dest_dir"
  for skill_dir in "$SKILLS_DIR"/*; do
    [ -d "$skill_dir" ] || continue
    [ -f "$skill_dir/SKILL.md" ] || continue
    install_one_skill "$skill_dir" "$dest_dir"
  done
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --global)
      MODE="global"
      PROJECT_DIR=""
      shift
      ;;
    --local|--project)
      MODE="local"
      [ "$#" -ge 2 ] || die "--local requires a project path"
      PROJECT_DIR="$2"
      shift 2
      ;;
    --target|--host)
      [ "$#" -ge 2 ] || die "--target requires codex, claude, agents, or all"
      TARGET="$2"
      shift 2
      ;;
    --copy)
      COPY=1
      shift
      ;;
    --force)
      FORCE=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --list)
      LIST_ONLY=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
done

[ -d "$SKILLS_DIR" ] || die "missing skill directory: $SKILLS_DIR"

if [ "$LIST_ONLY" -eq 1 ]; then
  list_skills
  exit 0
fi

case "$TARGET" in
  codex|claude|agents|all) ;;
  *) die "--target must be codex, claude, agents, or all" ;;
esac

if [ "$MODE" = "local" ]; then
  [ -n "$PROJECT_DIR" ] || die "--local requires a project path"
  if [ "$DRY_RUN" -eq 1 ]; then
    case "$PROJECT_DIR" in
      /*) ;;
      *) PROJECT_DIR="$(pwd -P)/$PROJECT_DIR" ;;
    esac
  else
    mkdir -p "$PROJECT_DIR"
    PROJECT_DIR=$(CDPATH= cd -- "$PROJECT_DIR" && pwd -P)
  fi
fi

case "$TARGET" in
  all)
    install_target codex "$PROJECT_DIR"
    install_target claude "$PROJECT_DIR"
    install_target agents "$PROJECT_DIR"
    ;;
  *)
    install_target "$TARGET" "$PROJECT_DIR"
    ;;
esac

if [ "$DRY_RUN" -eq 1 ]; then
  printf 'dry run complete\n'
else
  printf 'installed\n'
fi
