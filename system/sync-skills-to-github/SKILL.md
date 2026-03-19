---
name: sync-skills-to-github
description: Sync local Codex and Claude skills from a project into the GitHub repository for Yan9U, especially ai-skills-library. Use when the user asks to update, publish, push, or synchronize skill changes from `.codex/skills/` or `.claude/skills/` into GitHub with the correct repo structure, commit, and push.
---

# Sync Skills To GitHub

Use this skill when the user wants local skill changes synced to GitHub so the updated skill can be reused later from Codex or Claude Code.

## Default Target

- Default local source project: current workspace
- Default target repo path: `/home/yangu/Desktop/ai-skills-library`
- Default remote: `git@github.com:Yan9U/ai-skills-library.git`
- Default branch: `main`

If the user names a different target repo, use that instead.

## Workflow

1. Discover the local skill variants and the target repo path.
   Run `scripts/discover_skill_sync_targets.py` first.
2. Inspect git preflight in the target repo.
   Check `git status --short --branch` and `git remote -v`.
3. Respect the target repo's structure.
   If the target repo stores a shared skill source in a category directory such as `system/<skill-name>`, update that shared directory instead of creating duplicate `.codex` and `.claude` directories.
   Only create platform-specific directories when the target repo already uses that structure or the user explicitly asks for it.
4. Merge local Codex and Claude changes into the target skill.
   Read the local `.codex` and `.claude` versions plus the target repo version.
   Bring over substantive workflow, reference, and script improvements from both local variants.
   When the target repo is shared across agents, normalize platform-specific wording into neutral wording such as `the agent`, generic install paths, and helper names that are not tied to only Codex or only Claude.
5. Keep the write scope tight.
   Stage only the intended skill files.
   Do not rewrite unrelated repo content.
6. Validate before push.
   For changed Python scripts, run `python3 -m py_compile <script>`.
   Remove generated caches such as `__pycache__` before committing.
7. Sync safely.
   Run `git fetch origin` and, if needed, `git pull --ff-only origin main` before pushing.
   Commit with a narrow message such as `Update <skill-name> skill guidance`.
   Push with `git push origin main`.

## Rules

- Prefer the existing GitHub repo structure over the local project structure.
- Treat `.codex` and `.claude` as inputs when the target repo is shared-source.
- Preserve platform-specific metadata only when the target repo has a platform-specific home for it.
- Never use force push.
- If the target repo contains new upstream commits, fast-forward first.
- If multiple local skills are present and the user did not specify one, ask which skill to sync only when automatic selection would be risky. Otherwise sync the changed or named skill.

## Resources

- `references/repo-conventions.md`: Target repo defaults and merge rules
- `scripts/discover_skill_sync_targets.py`: Locate local skill variants and matching target skill directory

