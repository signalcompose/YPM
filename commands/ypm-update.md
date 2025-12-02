---
description: "Scan all projects and update PROJECT_STATUS.md"
---

Scan all projects and update `PROJECT_STATUS.md`.

**Execution Steps**:
1. Run `python scripts/scan_projects.py` to collect project information
   - Git worktree detection (.git file/directory)
   - Project classification (active/developing/inactive)
2. Read scan results (JSON format)
3. Collect detailed info from `CLAUDE.md` for active projects
4. Update `PROJECT_STATUS.md` in human-readable format
   - Add "(Git worktree)" to project name for worktrees
5. Complete

**Important**: This command does **NOT** perform Git operations. `PROJECT_STATUS.md` is updated as a local file only (`.gitignore`d).

**Notes**:
- Other project files are read-only (modification prohibited)
- Only YPM's own files can be modified
- Scan script automatically detects new projects
- PROJECT_STATUS.md is not Git-managed (daily operational task)

**CRITICAL: Accuracy Requirements**:
- **"Next task" should ONLY be obtained from**:
  - GitHub Issues (`gh issue list` command)
  - Latest commit messages
  - Content explicitly stated in project's CLAUDE.md, README.md
- **NEVER do**:
  - Create non-existent features or plans
  - Mark unimplemented features as "in progress"
  - Guess "next tasks" not documented
- **When unknown**: Honestly write "unknown", "not documented", or "no GitHub Issue found"
