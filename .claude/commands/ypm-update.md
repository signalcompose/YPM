<!-- Language Handling: Check ~/.ypm/config.yml for settings.language -->
<!-- If language is not "en", translate all output to that language -->

Scan all projects and update `PROJECT_STATUS.md`.

**Execution Steps**:
1. Run `python scripts/scan_projects.py` to collect project information
   - Git worktree detection (determined by .git file/directory)
   - Project classification (active/developing/dormant)
2. Read scan results (JSON format)
3. Collect detailed information from `CLAUDE.md` for active projects
4. Update `PROJECT_STATUS.md` in human-readable format
   - For worktrees, add "(Git worktree)" to project name
5. Complete

**Important**: This command **does not perform Git operations**. `PROJECT_STATUS.md` is updated as a local file (already in `.gitignore`).

**Notes**:
- Other project files are read-only (modification prohibited)
- Only YPM's own files can be modified
- The scan script automatically detects new projects
- PROJECT_STATUS.md is not under Git management (for routine operational tasks)

**CRITICAL: Ensuring Accuracy**:
- **"Next tasks" must be obtained ONLY from the following sources**:
  - GitHub Issues (`gh issue list` command)
  - Latest commit messages
  - Content explicitly stated in project's CLAUDE.md, README.md
- **Absolutely prohibited**:
  - Making up non-existent features or plans
  - Listing unimplemented features as "in progress"
  - Writing "next tasks" by guessing when not documented
- **When uncertain**: Honestly state "Unknown", "Not documented", or "No matching GitHub Issue"
