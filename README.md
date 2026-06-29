# Codex Skill Builder

Turn rough workflows, docs, scripts, and messy ideas into production-ready Codex skills.

Most people can use Codex. Fewer people know how to package a workflow so Codex can repeat it reliably. This skill helps you turn that repeatable work into a clean, installable skill with `SKILL.md`, references, scripts, examples, and validation.

## What It Does

- Designs a Codex skill from a vague idea or repeated workflow.
- Converts README/API/CLI docs into skill instructions.
- Reviews existing skills for trigger quality, structure, safety, and Codex fit.
- Scaffolds `SKILL.md`, `references/`, `scripts/`, `assets/`, and examples when useful.
- Validates the result with a lightweight Python checker.

## Quick Demo

Prompt:

```text
Use codex-skill-builder. I want a skill that summarizes Douyin videos from links, screenshots, or pasted subtitles.
```

The skill guides Codex to:

1. ask a compact Need Snapshot instead of a long interrogation;
2. infer the missing defaults;
3. propose a simple and stronger architecture;
4. generate a workspace preview copy;
5. add safety boundaries for scraping, copyright, and private data;
6. validate the final skill folder.

## Install

Using the Codex skill installer:

```text
Install from:
https://github.com/czy112603-ui/codex-skill-builder/tree/main/skills/codex-skill-builder
```

Manual install:

```powershell
Copy-Item -Recurse ".\skills\codex-skill-builder" "$env:CODEX_HOME\skills\codex-skill-builder"
```

Restart Codex after installing a new skill.

## Usage Examples

```text
Use codex-skill-builder to turn my release checklist into a Codex skill.
```

```text
Review this existing skill folder for structure, trigger quality, and safety boundaries:
D:\path\to\my-skill
```

```text
Convert this CLI README into a Codex skill that can operate the tool safely.
```

More examples are in [examples/prompts.md](examples/prompts.md).

## Repository Layout

```text
codex-skill-builder/
  README.md
  LICENSE
  examples/
    prompts.md
    before-after.md
  skills/
    codex-skill-builder/
      SKILL.md
      agents/
        openai.yaml
      references/
      scripts/
        quick_validate.py
        package_skill.py
```

## Why This Exists

Codex skills are best when they are small, repeatable, and explicit about when to trigger. In practice, many useful workflows start as messy notes:

- "Every week I do this manual audit."
- "I always ask Codex to follow these 12 steps."
- "This README is enough for a human, but Codex keeps missing edge cases."
- "I built a skill, but I do not know if it is packaged correctly."

This skill gives Codex a reusable process for turning those rough inputs into maintainable skills.

## Safety Defaults

The generated or reviewed skills should add boundaries for risky operations:

- no destructive file/database operations without confirmation;
- no private-data scraping;
- no credential leakage;
- no paid API calls without cost/rate-limit notes;
- no publishing, uploading, or external writes unless the user explicitly asks.

## Validate

From the repository root:

```powershell
python .\skills\codex-skill-builder\scripts\quick_validate.py .\skills\codex-skill-builder
```

Package a `.skill` zip:

```powershell
python .\skills\codex-skill-builder\scripts\package_skill.py .\skills\codex-skill-builder .\dist
```

## Launch Copy

Use this if you are sharing the project:

```text
I made a Codex skill that builds other Codex skills from messy workflows, docs, scripts, and rough ideas.

It asks the right setup questions, proposes a skill architecture, generates a workspace preview, adds safety boundaries, and validates the result.

Repo: https://github.com/czy112603-ui/codex-skill-builder
```

## License

MIT. See [LICENSE](LICENSE).
