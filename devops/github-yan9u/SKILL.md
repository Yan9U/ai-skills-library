---
name: github-yan9u
description: Use when cloning, creating, pulling, pushing, syncing, or wiring GitHub repositories owned by GitHub user Yan9U. Use gh for creating remote GitHub repositories and repository metadata operations, and use SSH git remotes in the form git@github.com:Yan9U/<repo>.git for day-to-day pull and push tasks in Codex or Claude Code.
---

# GitHub Workflow For Yan9U

Use this skill for repository sync tasks against GitHub account `Yan9U`.

## Environment facts

- GitHub SSH auth is available for `git@github.com`.
- GitHub CLI `gh` is installed locally.
- Global git identity is already configured for this account.

## Tool choice

- Use `gh` when a task needs GitHub API actions such as creating a remote repo.
- Use `git` for local repo inspection, branch work, fetch, pull, and push.
- Prefer SSH remotes even when the repo was created via `gh`.

## Required auth checks

Before using `gh` for remote-repo actions:

```bash
gh auth status
```

If not authenticated, complete the one-time login:

```bash
gh auth login --hostname github.com --git-protocol ssh --web
gh auth setup-git
```

After login, verify:

```bash
gh auth status
ssh -o BatchMode=yes -T git@github.com
```

## Remote format

Prefer SSH remotes for Yan9U-owned repositories:

```bash
git@github.com:Yan9U/<repo>.git
```

If a repo uses HTTPS and should point to Yan9U's GitHub, switch it to SSH:

```bash
git remote set-url origin git@github.com:Yan9U/<repo>.git
```

## Required preflight

Before any push or pull, inspect the repo state:

```bash
git status --short --branch
git remote -v
```

If the remote is missing:

```bash
git remote add origin git@github.com:Yan9U/<repo>.git
```

## Common tasks

Clone a Yan9U repository:

```bash
git clone git@github.com:Yan9U/<repo>.git
```

Create a remote GitHub repository under Yan9U:

```bash
gh repo create Yan9U/<repo> --private --clone=false
```

Create a public remote repository instead:

```bash
gh repo create Yan9U/<repo> --public --clone=false
```

Create a remote repository from the current local directory, add `origin`, and push:

```bash
gh repo create Yan9U/<repo> --source=. --remote=origin --private --push
```

If the local repo already exists and should attach to a freshly created remote without immediate push:

```bash
gh repo create Yan9U/<repo> --private --clone=false
git remote add origin git@github.com:Yan9U/<repo>.git
git push -u origin HEAD
```

Fetch everything and prune stale refs:

```bash
git fetch --all --prune
```

Pull the current branch safely:

```bash
git pull --ff-only origin <branch>
```

Push the current branch and set upstream:

```bash
git push -u origin HEAD
```

Push a named branch:

```bash
git push -u origin <branch>
```

Show the current branch name before push/pull if needed:

```bash
git branch --show-current
```

## New repo setup from an existing local directory

If the local project should connect to a Yan9U repo:

```bash
git init
git branch -M main
gh repo create Yan9U/<repo> --source=. --remote=origin --private --push
```

If the repo is already initialized locally:

```bash
git branch -M main
gh repo create Yan9U/<repo> --source=. --remote=origin --private --push
```

## Working rules

- Prefer `git pull --ff-only` over merge pulls.
- Prefer `git push -u origin HEAD` when pushing the current checked-out branch.
- Prefer `gh repo create Yan9U/<repo> --source=. --remote=origin --private --push` for first-time publication of a local repo.
- Never use `git push --force` or `git push --force-with-lease` unless the user explicitly asks.
- Never rewrite remotes or branches unless they clearly map to Yan9U's intended repo.
- If auth unexpectedly fails, verify with:

```bash
ssh -o BatchMode=yes -T git@github.com
```

Expected success output includes:

```text
Hi Yan9U! You've successfully authenticated, but GitHub does not provide shell access.
```

If GitHub CLI auth unexpectedly fails, re-run:

```bash
gh auth status
gh auth login --hostname github.com --git-protocol ssh --web
```
