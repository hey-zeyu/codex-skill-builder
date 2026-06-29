# Before And After

This example shows how a rough idea becomes a skill-ready workflow.

## Before

```text
I want Codex to help me make skills. Usually I have an idea, maybe a README, maybe some scripts. I want it to ask questions, create the files, and check if the skill is good.
```

## Codex Skill Builder Response Shape

```text
Need Snapshot:
1. What should trigger this skill?
2. What inputs will users provide?
3. What output should the skill produce?
4. What steps are repeated manually?
5. What must the skill never do without confirmation?
6. What does success look like?
```

After the user answers, Codex Skill Builder proposes:

- known needs and missing details;
- simple vs stronger architecture;
- recommended first version;
- concrete workflow;
- workspace preview as the default build target.

## After

```text
codex-skill-builder/
  SKILL.md
  agents/openai.yaml
  references/best-practices.md
  references/workflows.md
  references/output-patterns.md
  references/interaction-guide.md
  scripts/quick_validate.py
  scripts/package_skill.py
```

The result is a reusable skill that another Codex session can load, follow, and validate.
