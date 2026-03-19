# Repo Conventions

## Target Defaults

- Target repo path: `/home/yangu/Desktop/ai-skills-library`
- Target remote: `git@github.com:Yan9U/ai-skills-library.git`
- Target branch: `main`

## Shared-Source Rule

`ai-skills-library` is organized by category folders such as `system/`, `devops/`, and `scientific-research/`.

For this repo:

- Find the target skill by matching the `name:` field in `SKILL.md`
- Update the shared source directory if it already exists
- Do not create `.codex/skills/...` or `.claude/skills/...` inside that repo unless the repo later adopts that structure

## Merge Rule

When local `.codex` and `.claude` versions differ:

- Keep shared workflow improvements from both
- Convert platform-specific wording into neutral shared wording
- Preserve platform-specific details only when they map to an existing target file

Examples of neutral wording:

- `the agent` instead of `Codex` or `Claude`
- `<installed-skill-dir>` instead of a hard-coded `.codex/...` path inside shared docs
- `AI Skill Helper` instead of an agent-specific helper label in generated metadata

