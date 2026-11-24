"""Load agent instructions from .agents/skills/, memory.md, and schema.json."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = PROJECT_ROOT / ".agents" / "skills"


def read_skill(skill_folder: str) -> str:
    """Return the markdown body of a skill without YAML frontmatter."""
    skill_path = SKILLS_DIR / skill_folder / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].strip()
    return text.strip()


def read_memory() -> str:
    """Return short team memory read by Lead before every run."""
    return (PROJECT_ROOT / "memory.md").read_text(encoding="utf-8").strip()


def read_schema_text() -> str:
    """Return content.json schema text."""
    return (PROJECT_ROOT / "schema.json").read_text(encoding="utf-8").strip()


def build_instruction(skill_folder: str, extra_context: str = "") -> str:
    """Compose an agent instruction using its SKILL.md as single source of truth."""
    parts = [read_skill(skill_folder)]
    if extra_context:
        parts.append(extra_context.strip())
    return "\n\n---\n\n".join(parts)
