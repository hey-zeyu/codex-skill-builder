#!/usr/bin/env python3
"""
Initialize a Codex skill folder.
"""

import argparse
import re
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: {description}
---

# {skill_title}

Use this skill when {when_to_use}.

## Workflow

1. Understand the user's input and intended output.
2. Choose the shortest reliable path.
3. Use bundled references or scripts only when they materially help.
4. Validate the result before reporting completion.

## Output

Return the result in the format the user requested. If no format is specified, use concise Markdown.

## Safety

- Ask before overwriting, deleting, publishing, uploading, or spending money.
- Do not expose API keys, tokens, private data, or credentials.
- Follow platform and copyright restrictions when processing external content.
"""


OPENAI_YAML_TEMPLATE = """display_name: {display_name}
short_description: {short_description}
default_prompt: Help me use this skill on my current task.
"""


REFERENCE_TEMPLATE = """# Usage Notes

Add detailed usage guidance here only when the information is too long for SKILL.md.

Keep references one level deep from SKILL.md.
"""


SCRIPT_TEMPLATE = '''#!/usr/bin/env python3
"""
Smoke test for {skill_name}.
"""

from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    required = [root / "SKILL.md"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("Missing required files:")
        for item in missing:
            print(f"- {{item}}")
        return 1
    print("Smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def title_case(name):
    return " ".join(part.capitalize() for part in name.split("-"))


def validate_name(name):
    if not re.match(r"^[a-z0-9-]+$", name):
        raise ValueError("Skill name must use lowercase letters, digits, and hyphens only")
    if name.startswith("-") or name.endswith("-") or "--" in name:
        raise ValueError("Skill name cannot start/end with hyphen or contain --")
    if len(name) > 64:
        raise ValueError("Skill name must be 64 characters or fewer")


def init_skill(args):
    validate_name(args.name)
    out_dir = Path(args.path).resolve() / args.name
    if out_dir.exists():
        raise FileExistsError(f"Skill directory already exists: {out_dir}")

    out_dir.mkdir(parents=True)
    display_name = title_case(args.name)
    description = args.description or (
        f"{display_name} skill. Use when the user asks for this workflow or related tasks."
    )
    when_to_use = args.when or "the user asks for this workflow or related tasks"

    (out_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(
            skill_name=args.name,
            skill_title=display_name,
            description=description,
            when_to_use=when_to_use,
        ),
        encoding="utf-8",
    )

    agents_dir = out_dir / "agents"
    agents_dir.mkdir()
    (agents_dir / "openai.yaml").write_text(
        OPENAI_YAML_TEMPLATE.format(
            display_name=display_name,
            short_description=description[:120],
        ),
        encoding="utf-8",
    )

    if "references" in args.resources:
        references_dir = out_dir / "references"
        references_dir.mkdir()
        (references_dir / "usage.md").write_text(REFERENCE_TEMPLATE, encoding="utf-8")

    if "scripts" in args.resources:
        scripts_dir = out_dir / "scripts"
        scripts_dir.mkdir()
        smoke = scripts_dir / "smoke_test.py"
        smoke.write_text(SCRIPT_TEMPLATE.format(skill_name=args.name), encoding="utf-8")
        smoke.chmod(0o755)

    if "assets" in args.resources:
        (out_dir / "assets").mkdir()

    print(f"Created Codex skill: {out_dir}")
    return out_dir


def main():
    parser = argparse.ArgumentParser(description="Initialize a Codex skill folder")
    parser.add_argument("name", help="Skill name in hyphen-case")
    parser.add_argument("--path", required=True, help="Directory where the skill is created")
    parser.add_argument("--description", default="", help="Frontmatter description")
    parser.add_argument("--when", default="", help="Plain-language use case")
    parser.add_argument(
        "--resources",
        default="references,scripts",
        help="Comma-separated resources: references,scripts,assets",
    )
    args = parser.parse_args()
    args.resources = {item.strip() for item in args.resources.split(",") if item.strip()}
    init_skill(args)


if __name__ == "__main__":
    main()
