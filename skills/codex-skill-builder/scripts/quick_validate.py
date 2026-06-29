#!/usr/bin/env python3
"""
Validate a Codex skill folder using only the Python standard library.
"""

import re
import sys
from pathlib import Path


ALLOWED_KEYS = {"name", "description"}


def parse_simple_frontmatter(text):
    if not text.startswith("---"):
        raise ValueError("No YAML frontmatter found")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    if not match:
        raise ValueError("Invalid frontmatter format")

    data = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        data[key] = value
    return data


def validate_skill(skill_path):
    skill_path = Path(skill_path)
    skill_md = skill_path / "SKILL.md"

    if not skill_path.exists():
        return False, f"Skill folder not found: {skill_path}"
    if not skill_path.is_dir():
        return False, f"Path is not a directory: {skill_path}"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter = parse_simple_frontmatter(content)
    except ValueError as exc:
        return False, str(exc)

    unexpected = set(frontmatter) - ALLOWED_KEYS
    if unexpected:
        return False, (
            "Unexpected frontmatter key(s): "
            + ", ".join(sorted(unexpected))
            + ". Allowed keys: name, description"
        )

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()

    if not name:
        return False, "Missing 'name' in frontmatter"
    if not description:
        return False, "Missing 'description' in frontmatter"
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, (
            f"Name '{name}' must use lowercase letters, digits, and hyphens only"
        )
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain --"
    if len(name) > 64:
        return False, f"Name is too long ({len(name)} chars); max is 64"
    if len(description) > 1024:
        return False, (
            f"Description is too long ({len(description)} chars); max is 1024"
        )
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"

    body = content.split("---", 2)[-1].strip()
    if not body:
        return False, "SKILL.md body is empty"

    return True, "Skill is valid"


def main():
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill-folder>")
        return 1

    valid, message = validate_skill(sys.argv[1])
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
