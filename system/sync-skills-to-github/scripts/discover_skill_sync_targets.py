#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_skill_name(skill_md: Path) -> str | None:
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return None


def collect_local_skills(project_root: Path) -> dict[str, dict[str, str]]:
    results: dict[str, dict[str, str]] = {}
    for platform in ("codex", "claude"):
        base = project_root / f".{platform}" / "skills"
        if not base.exists():
            continue
        for skill_md in base.glob("*/SKILL.md"):
            skill_name = parse_skill_name(skill_md)
            if not skill_name:
                continue
            results.setdefault(skill_name, {})[platform] = str(skill_md.parent.resolve())
    return results


def collect_repo_targets(repo_root: Path) -> dict[str, list[str]]:
    targets: dict[str, list[str]] = {}
    for skill_md in repo_root.rglob("SKILL.md"):
        if ".git" in skill_md.parts:
            continue
        skill_name = parse_skill_name(skill_md)
        if not skill_name:
            continue
        targets.setdefault(skill_name, []).append(str(skill_md.parent.resolve()))
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover local skill variants and matching target repo skill directories.")
    parser.add_argument("--project-root", default=".", help="Project root containing .codex/skills and .claude/skills")
    parser.add_argument("--repo", default="/home/yangu/Desktop/ai-skills-library", help="Target repo root")
    parser.add_argument("--skill", help="Optional skill name filter")
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    repo_root = Path(args.repo).expanduser().resolve()

    local_skills = collect_local_skills(project_root)
    repo_targets = collect_repo_targets(repo_root) if repo_root.exists() else {}

    skill_names = sorted(local_skills)
    if args.skill:
        skill_names = [name for name in skill_names if name == args.skill]

    result = []
    for skill_name in skill_names:
        local_entry = local_skills[skill_name]
        matches = repo_targets.get(skill_name, [])
        result.append(
            {
                "skill_name": skill_name,
                "local_codex_dir": local_entry.get("codex"),
                "local_claude_dir": local_entry.get("claude"),
                "target_matches": matches,
                "proposed_target_dir": str((repo_root / "system" / skill_name).resolve()),
            }
        )

    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
