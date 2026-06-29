# Codex Skill Builder

> Turn your messy workflow into a reusable Codex skill.

Most people ask Codex the same thing again and again.

This project helps you package that repeated work into a skill Codex can trigger, follow, validate, and improve.

In other words:

```text
rough idea / README / script / checklist
        -> Codex Skill Builder
        -> clean Codex skill
```

## Why It Matters

Codex is powerful, but repeated prompting is fragile.

A good skill is a reusable operating manual:

- it tells Codex when to wake up;
- it gives Codex the workflow it should follow;
- it keeps long knowledge in references;
- it stores repeatable actions in scripts;
- it adds safety boundaries before risky operations.

This skill is for turning "I keep doing this manually" into "Codex knows how to do this now."

## The Hook

You do not need to know how to design a skill.

Bring one of these:

- a rough idea;
- a repeated workflow;
- a README/API/CLI doc;
- a checklist;
- a script folder;
- an existing skill that feels messy.

Codex Skill Builder turns it into a structured skill with a sane first version.

## What You Get

### 1. Need Snapshot

Instead of asking 20 vague questions, it asks the few questions that actually change the design:

- What should trigger the skill?
- What input does the user provide?
- What output should it produce?
- What steps are repeated manually?
- What must it never do without confirmation?
- What does success look like?

### 2. Skill Architecture

It decides whether the skill should be:

- just `SKILL.md`;
- `SKILL.md` plus references;
- a fuller skill with references, scripts, examples, and validation.

### 3. Build + Review Loop

It can:

- scaffold a workspace preview copy;
- write a clean `SKILL.md`;
- move long guidance into `references/`;
- add scripts for repeatable operations;
- review trigger quality and safety;
- validate the final folder.

## Example

Prompt:

```text
Use codex-skill-builder. I want a skill that summarizes Douyin videos from links, screenshots, or pasted subtitles.
```

Codex Skill Builder will not rush into files.

It first asks for a Need Snapshot, then proposes a simple version and a stronger version, then waits for you to say `generate`.

That rhythm keeps the skill useful instead of overbuilt.

## Install

Install this skill from:

```text
https://github.com/hey-zeyu/codex-skill-builder/tree/main/skills/codex-skill-builder
```

Manual install:

```powershell
Copy-Item -Recurse ".\skills\codex-skill-builder" "$env:CODEX_HOME\skills\codex-skill-builder"
```

Restart Codex after installing a new skill.

## Use It For

```text
Use codex-skill-builder to turn my release checklist into a Codex skill.
```

```text
Use codex-skill-builder to convert this CLI README into a safe Codex skill.
```

```text
Use codex-skill-builder to review this skill folder for trigger quality, structure, and safety.
```

More examples: [examples/prompts.md](examples/prompts.md)

## Repository Structure

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
      agents/openai.yaml
      references/
      scripts/
```

## Design Principles

### Small First

Start with the smallest skill that can work. Add references, scripts, and assets only when they make the skill more repeatable.

### Clear Trigger

The description should make it obvious when Codex should use the skill.

### Progressive Disclosure

Keep `SKILL.md` lean. Move long rules, examples, and domain knowledge into one-level reference files.

### Safety Before Automation

Skills that delete, upload, scrape, spend money, call APIs, or touch private data should require confirmation and clear boundaries.

## Validate

```powershell
python .\skills\codex-skill-builder\scripts\quick_validate.py .\skills\codex-skill-builder
```

Package a `.skill` zip:

```powershell
python .\skills\codex-skill-builder\scripts\package_skill.py .\skills\codex-skill-builder .\dist
```

## Launch Copy

```text
I made a Codex skill that turns messy workflows, docs, scripts, and checklists into clean Codex skills.

It asks the right setup questions, proposes the skill architecture, generates a workspace preview, adds safety boundaries, and validates the result.

Repo: https://github.com/hey-zeyu/codex-skill-builder
```

## License

MIT. See [LICENSE](LICENSE).
