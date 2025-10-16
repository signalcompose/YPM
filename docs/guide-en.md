# YPM Detailed Guide (English)

> Complete usage guide for YPM (Your Project Manager)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [FAQ](#faq)
- [Future Enhancements](#future-enhancements)

---

## Overview

YPM is a tool that automatically collects and organizes the status of multiple projects within a specified directory and displays them in a unified view.

**Who is this tool for?**
- Engineers and creators working on multiple projects simultaneously
- People with side projects alongside their main work
- Managers overseeing multiple team projects

### Problems It Solves

- ✅ Too many projects to track which ones are active
- ✅ Difficult to remember the status of side projects
- ✅ Time-consuming to check what needs to be done next
- ✅ Hard to visualize progress and priorities

---

## Features

- **Automatic Collection**: Gathers information from Git history and documentation
- **Centralized Management**: All projects managed in a single file
- **Claude Code Integration**: Easy updates using Claude Code
- **Progress Visualization**: Displays progress metrics for each project
- **Next Task Identification**: Shows what to do next for each project
- **Flexible Configuration**: Customize monitoring targets via `config.yml`

---

## Prerequisites

- **Git**: Used for collecting project information
- **Claude Code**: Used for updating project status (recommended)
  - [Get Claude Code](https://claude.com/claude-code)
- **Python 3.8+**: For the onboarding wizard

---

## Installation

### 1. Clone the Repository

```bash
# Clone YPM
git clone https://github.com/signalcompose/YPM.git
cd YPM
```

### 2. Install Dependencies

```bash
# Install Python dependencies
pip3 install -r requirements.txt
```

**Required Dependencies**:
- Python 3.8+
- PyYAML (for reading/writing config.yml)

---

## Setup

### Using the Onboarding Wizard (Recommended)

YPM includes an interactive setup wizard. Simply run the following command for easy setup:

```bash
# Run the onboarding wizard
python3 scripts/onboarding.py
```

The wizard will interactively collect:
1. Path to the project directory to monitor
2. Project detection patterns (auto-suggested)
3. Classification threshold days for active/inactive status

Upon completion, `config.yml` will be automatically generated.

### Manual Setup (Advanced)

If you prefer manual setup without the wizard:

1. Copy `config.example.yml`

```bash
cp config.example.yml config.yml
```

2. Edit `config.yml`

```yaml
monitor:
  directories:
    - /path/to/your/projects    # Change to your project directory

  patterns:
    - "*"             # All projects directly under the directory
```

**Example (macOS/Linux)**:
```yaml
directories:
  - /Users/yourname/Projects
  - /Users/yourname/Work
```

**Example (Windows)**:
```yaml
directories:
  - C:/Users/yourname/Projects
```

### Initial Project Information Collection

Start Claude Code and instruct:

```
Update project status
```

This will generate `PROJECT_STATUS.md` with all project information collected.

---

## Usage

### 1. Check Project Status

```bash
cd ~/Src/proj_YPM/YPM
cat PROJECT_STATUS.md
```

View the status of all projects at a glance.

### 2. Update Status

```bash
cd ~/Src/proj_YPM/YPM
# Start Claude Code
```

Instruct Claude Code:

```
Update project status
```

This will automatically:
1. Scan directories specified in `config.yml`
2. Retrieve Git information for each project
3. Read documentation (CLAUDE.md, README.md, docs/INDEX.md)
4. Update `PROJECT_STATUS.md`
5. Commit changes

### 3. Check Next Tasks

```
What are the next tasks?
```

Displays next tasks for each project in priority order.

---

## Claude Code Custom Commands

YPM includes convenient custom commands that can be executed directly within Claude Code.

### Project Management Commands

#### `/ypm`
Displays a welcome message and list of frequently used commands. Useful when starting a session.

#### `/ypm-help`
Displays detailed help for all commands. You can view command descriptions, YPM principles, and common use cases.

#### `/ypm-update`
Scans all projects and updates `PROJECT_STATUS.md`.

**Actions performed**:
1. Scans monitoring target directories specified in `config.yml`
2. Retrieves Git information for each project (branch, last commit, changed files)
3. Reads `CLAUDE.md`, `README.md`, `docs/INDEX.md` from each project
4. Collects progress information (Phase, implementation progress, testing, documentation)
5. Updates `PROJECT_STATUS.md`
6. Commits changes

**Note**: Other projects' files are read-only (modification forbidden)

#### `/ypm-next`
Displays "next tasks" for each project in priority order.

**Display content**:
- Project name
- Current Phase
- Next task
- Last update date

**Priority order**:
1. Active projects (updated within the last week)
2. Projects with high implementation progress
3. Phase order

#### `/ypm-active`
Displays only active projects updated within the last week.

**Display content**:
- Project name, overview, branch
- Last update date, Phase, implementation progress
- Next task

Displayed in descending order of update date (newest first).

### New Project Setup Command

#### `/ypm-new`
Launches an interactive wizard to help set up new projects.

Sets up projects step-by-step through 8 phases:
1. **Project Planning**: Requirements definition, technology selection
2. **Directory Creation**: Local directory creation and Git initialization
3. **Documentation Setup**: Development environment based on DDD/TDD/DRY principles
4. **GitHub Integration**: Remote repository creation and initial push
5. **Git Workflow Setup**: Branch strategy and rule establishment
6. **Environment Configuration**: `.gitignore`, `.claude/settings.json`
7. **Documentation Management Rules**: Synchronization between implementation and documentation
8. **Final Confirmation**: Ready to start development

**After setup completion**:
- Move to the new project directory
- Start development in a dedicated Claude Code session for that project
- YPM will automatically add it to monitoring targets on the next `/ypm-update`

See [project-bootstrap-prompt.md](../project-bootstrap-prompt.md) for details.

---

## Project Bootstrap Assistant

YPM includes a comprehensive assistant feature for launching new projects.

### How to Use

Two methods are available:

**Method 1: Use Custom Command (Recommended)**

Execute in Claude Code:
```
/ypm-new
```

**Method 2: Use Prompt Manually**

1. Copy the contents of `project-bootstrap-prompt.md`
2. Paste into Claude Code
3. Follow the interactive wizard through 8 phases

### Features

- **Comprehensive Support from Requirements to Setup**
  - Project planning interviews
  - Requirements and specification documents
  - Proper directory structure

- **Introduction of Development Best Practices**
  - DDD (Domain-Driven Design)
  - TDD (Test-Driven Development)
  - DRY (Don't Repeat Yourself) principle

- **Git Workflow Configuration**
  - Git Flow support
  - Git Worktree support (optional)
  - Branch protection rules

- **Documentation Management Rules**
  - Synchronization between implementation and documentation
  - Onboarding support
  - PR templates and checklists

### Introduced Development Principles

#### DDD (Domain-Driven Design)
- Layer structure definition (Domain, Application, Infrastructure, Presentation)
- Directory structure guidelines

#### TDD (Test-Driven Development)
- Red → Green → Refactor cycle adherence
- Culture of writing tests before implementation
- Test coverage goal setting

#### DRY (Don't Repeat Yourself)
- Avoid code duplication
- Extract common logic
- Reusable component design

### Generated Documentation

The following documentation is created during project setup:

- `README.md` - Project overview, setup instructions
- `docs/requirements.md` - Requirements specification
- `docs/specifications.md` - System specifications
- `docs/architecture.md` - Architecture design
- `docs/development-guide.md` - Development guidelines
- `docs/onboarding.md` - Onboarding guide for new members
- `.claude/settings.json` - Claude Code permissions
- `.gitignore` - Git exclusion settings

---

## File Structure

```
YPM/
├── .claude/
│   └── settings.json           # Claude Code permissions
├── docs/
│   ├── INDEX.md                # Documentation index
│   ├── guide-ja.md             # Japanese detailed guide
│   ├── guide-en.md             # English detailed guide (this file)
│   └── development/            # Developer documentation
│       ├── architecture.md     # Architecture design
│       └── onboarding-script-spec.md  # Onboarding specification
├── scripts/
│   ├── onboarding.py           # Initial setup wizard
│   ├── update_status.py        # Project status update (future)
│   └── create_project.py       # Project creation support (future)
├── config.yml                  # Configuration file (monitoring targets) *Git-ignored
├── config.example.yml          # Configuration template
├── requirements.txt            # Python dependencies
├── CLAUDE.md                   # Claude Code instructions
├── README.md                   # Project overview (English)
├── PROJECT_STATUS.md           # Project status list *Git-ignored
├── LICENSE                     # MIT License
└── .gitignore                  # Git exclusion settings
```

---

## Project Categories

### 🔥 Active Projects
Projects updated within the last week. Currently in progress.

### 🎨 Planning Stage
Projects in Phase 0 or documentation phase. Pre-implementation.

### 🚧 In Development
Implementation in progress but no updates in over a week.

### 💤 Inactive
No updates for over 1 month. Temporarily paused.

### 📦 Non-Git
Not a Git repository. Not tracked for progress.

---

## Progress Calculation Criteria

YPM estimates project progress based on the following criteria:

| Progress | Phase | Status |
|----------|-------|--------|
| 0-20% | Phase 0 | Design/Planning |
| 20-30% | Phase 1 | Development Environment Setup |
| 30-60% | Phase 2-3 | Basic Feature Implementation |
| 60-80% | Phase 4-5 | Testing/Improvement |
| 80-100% | Phase 6+ | Production/Feature Expansion |

**Note**: These are estimated values. Manually adjust if they don't match reality.

---

## Customization

### Adding Monitoring Targets

Add to `directories` in `config.yml`:

```yaml
monitor:
  directories:
    - /Users/yamato/Src
    - /Users/yamato/Work      # Add
    - /Users/yamato/Projects  # Add
```

### Changing Project Detection Patterns

For different directory structures:

```yaml
monitor:
  patterns:
    - "proj_*/*"          # 2-level structure
    - "projects/*"        # 1-level structure
    - "my-apps/*/src"     # 3-level structure
```

### Changing Classification Criteria

Modify active/inactive threshold days:

```yaml
classification:
  active_days: 14    # Change to 2 weeks for active
  inactive_days: 60  # Change to 2 months for inactive
```

---

## Update Frequency

- **Recommended**: Once a week
- **Minimum**: Once a month

Regular updates help you stay on top of project status.

---

## FAQ

### Q: How do I add a new project?

**A**: Create a project under the directory specified in `config.yml`, and it will be automatically detected on the next update.

### Q: How do I exclude a project?

**A**: Add to `exclude` in `config.yml`:

```yaml
monitor:
  exclude:
    - proj_YPM/YPM
    - old_projects/*   # Pattern to exclude
```

### Q: Progress percentages are inaccurate

**A**: Manually edit `PROJECT_STATUS.md` to adjust them.

### Q: Next tasks are not displayed

**A**: Add development plans to the project's `CLAUDE.md` or `docs/`. YPM will read and display them.

### Q: Can I use this on another machine?

**A**: Yes. Update directory paths in `config.yml` to match your environment. Since it's managed via Git, syncing is easy.

---

## Future Enhancements

YPM is currently at **Phase 1 completion**. The Claude Code-driven approach has proven effective in production use.

Potential future enhancements:

- [ ] Project creation support tool
- [ ] Dashboard UI (web-based)
- [ ] Slack notification integration
- [ ] Automatic priority calculation
- [ ] Gantt chart generation
- [ ] Inter-project dependency visualization

**Note**: Automated update scripts (cron support) are currently deprioritized, as AI-based contextual understanding and flexible task extraction are superior.

---

## Troubleshooting

### Q: Project not detected

**A**: Check the following:
1. Is it a Git repository? (Does `.git/` directory exist?)
2. Does the directory structure match the configured pattern?
3. Is it included in the exclusion list?

### Q: Claude Code tries to modify configuration files

**A**: Set read-only permissions in `.claude/settings.json`. Allow changes only to YPM's own files.

---

## Contributing

Contributions to YPM are welcome!

### Bug Reports & Feature Requests

- Report via [GitHub Issues](https://github.com/signalcompose/YPM/issues)

### Pull Requests

1. Fork this repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a pull request

### Development Guidelines

See `CONTRIBUTING.md` (to be created) for details.

---

## License

This project is licensed under the [MIT License](../LICENSE).

---

## Author

**Hiroshi Yamato / dropcontrol**

- Website: [hiroshiyamato.com](https://hiroshiyamato.com/) | [yamato.dev](https://yamato.dev/)
- X: [@yamato](https://x.com/yamato)
- GitHub: [dropcontrol](https://github.com/dropcontrol)

Powered by Claude Code

---

## Related Documentation

- **[README.md](../README.md)** - Project overview (English)
- **[詳細ガイド（日本語）](guide-ja.md)** - Japanese detailed guide
- **[CLAUDE.md](../CLAUDE.md)** - Claude Code instructions
- **[docs/INDEX.md](INDEX.md)** - Documentation index

---

**Manage your projects, simplified.** 🚀
