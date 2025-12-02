<!-- Language Handling: Check ~/.ypm/config.yml for settings.language -->
<!-- If language is not "en", translate all output to that language -->

# YPM (Your Project Manager) - Help

## Overview

YPM monitors multiple projects under your configured directories and provides centralized progress management.

---

## Available Commands

### Project Management

#### `/ypm`
Displays the welcome message and common commands list.

#### `/ypm-update`
Scans all projects and updates `PROJECT_STATUS.md`.
- Retrieves Git information for each project
- Reads CLAUDE.md, README.md, docs/INDEX.md
- Collects progress information (Phase, implementation progress, tests, documentation)
- Commits changes

#### `/ypm-next`
Displays "next tasks" for each project in priority order.
- Active projects (updated within the last week)
- Projects with higher implementation progress
- Phase order

#### `/ypm-active`
Shows only active projects updated within the last week.
- Project name, overview, branch, last update date
- Phase, implementation progress, next task

---

### New Projects

#### `/ypm-new`
Assists with launching new projects.
- Project planning (requirements definition, technology selection)
- Directory creation and Git initialization
- Documentation setup (DDD/TDD/DRY principles)
- GitHub integration
- Git Workflow configuration
- Environment configuration file setup

See `project-bootstrap-prompt.md` for details.

---

### Help

#### `/ypm-help`
Displays this help message.

---

## YPM Principles

### Read-Only
YPM monitors other projects in **read-only** mode. Only YPM's own files can be modified.

### Role Division
- **YPM**: Project monitoring, progress management, new project launch support
- **Each Project**: Implementation, development, testing (conducted in dedicated Claude Code sessions for each project)

---

## Reference Documentation

- **CLAUDE.md** - YPM project instructions
- **project-bootstrap-prompt.md** - New project launch guide
- **config.example.yml** - Sample configuration file

---

## Common Usage

### 1. At Session Start
```
/ypm
```
Display the welcome message to see available options.

### 2. Check Project Status
```
/ypm-update
```
Scan all projects to get the latest status.

### 3. Know What to Do Next
```
/ypm-next
```
Check high-priority tasks.

### 4. Start a New Project
```
/ypm-new
```
Set up a project interactively.

---

**Manage multiple projects efficiently with YPM!**
