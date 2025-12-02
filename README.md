# YPM (Your Project Manager)

> Multi-project progress tracking system powered by Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## What is YPM?

YPM is a project management tool that automatically tracks the status of multiple projects in a specified directory.

**Key Features**:
- Automatic information collection from Git history and documentation
- Centralized management of all projects in a single file (`PROJECT_STATUS.md`)
- Progress visualization with multiple metrics (Phase, Implementation, Testing, Documentation)
- Next task identification for each project
- Flexible configuration via `config.yml`

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/signalcompose/YPM.git
cd YPM
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Run the onboarding wizard

```bash
python3 scripts/onboarding.py
```

The wizard will guide you through:
- Setting the directory to monitor
- Configuring project detection patterns
- Setting activity classification thresholds

### 4. Update project status

Open Claude Code in the YPM directory and say:

```
Update project status
```

This will scan all projects and generate `PROJECT_STATUS.md`.

---

## Installation as Claude Code Plugin (Recommended)

YPM can be installed as a Claude Code plugin, making it accessible from **any directory**.

### Step 1: Install the Plugin

```bash
# In Claude Code, run:
/plugin marketplace add signalcompose/YPM
/plugin install ypm@signalcompose-ypm
```

### Step 2: Initial Setup

```bash
# Run the setup wizard (from any directory)
/ypm:ypm-setup
```

This creates `~/.ypm/` with your configuration:
- `~/.ypm/config.yml` - Your monitoring settings
- `~/.ypm/PROJECT_STATUS.md` - Generated project status

### Step 3: Start Using

```bash
# Scan your projects
/ypm:ypm-update

# View next tasks
/ypm:ypm-next

# Show active projects
/ypm:ypm-active
```

### Available Commands

All commands are prefixed with `ypm:` when installed as a plugin:

| Command | Description |
|---------|-------------|
| `/ypm:ypm-setup` | Initial setup wizard |
| `/ypm:ypm` | Show welcome and quick commands |
| `/ypm:ypm-help` | Show detailed help |
| `/ypm:ypm-update` | Update project status |
| `/ypm:ypm-next` | Show next tasks |
| `/ypm:ypm-active` | Show active projects only |
| `/ypm:ypm-open` | Open project in editor |
| `/ypm:ypm-new` | Launch project setup wizard |
| `/ypm:ypm-export-community` | Export to community version |
| `/ypm:ypm-trufflehog-scan` | Run security scan |

### Optional: Prefix-Free Commands

During setup, you can optionally create symlinks to `~/.claude/commands/` for prefix-free access:

```bash
# With symlinks, you can use:
/ypm-update    # instead of /ypm:ypm-update
/ypm-next      # instead of /ypm:ypm-next
```

### Data Location

YPM stores all user data in `~/.ypm/`:

```
~/.ypm/
  ├── config.yml           # Your monitoring settings
  └── PROJECT_STATUS.md    # Generated project status
```

This separation ensures:
- Plugin updates don't affect your configuration
- Easy backup (just backup `~/.ypm/`)
- Works across all your projects

---

## Documentation

- **[Detailed Guide (English)](docs/guide-en.md)** - Complete usage guide
- **[詳細ガイド（日本語）](docs/guide-ja.md)** - 日本語の詳細ガイド
- **[Security Policy](SECURITY.md)** - Security considerations and best practices

---

## How It Works

1. **Scans** directories specified in `config.yml`
2. **Collects** Git information (branch, commits, changes)
3. **Reads** project documentation (CLAUDE.md, README.md, docs/)
4. **Generates** `PROJECT_STATUS.md` with categorized project status

---

## Project Categories

- **🔥 Active**: Updated within 1 week
- **🎨 Planning**: In design phase (Phase 0)
- **🚧 In Development**: Implementation in progress
- **💤 Inactive**: No updates for over 1 month
- **📦 Non-Git**: Not a Git repository

---

## Requirements

- **Git**: For project information collection
- **Claude Code**: For project status updates (recommended)
  - [Get Claude Code](https://claude.com/claude-code)
- **Python 3.8+**: For onboarding wizard

---

## Claude Code Custom Commands

YPM includes custom slash commands for quick operations:

### Project Management
- `/ypm` - Show welcome message and quick commands
- `/ypm-help` - Show detailed help with all available commands
- `/ypm-update` - Update project status (scan all projects)
- `/ypm-next` - Show next tasks for all projects in priority order
- `/ypm-active` - Show only active projects (updated within 1 week)
- `/ypm-open [project] [editor] [options]` - Open a project in your preferred editor
  - **Basic usage**:
    - No arguments: Show project list (excluding ignored, worktrees auto-excluded)
    - `<project>`: Open project with default editor
    - `<project> <editor>`: Open project with specific editor (code/cursor/zed)
  - **Editor settings**:
    - `--editor`: Show current default editor
    - `--editor <name>`: Set default editor (code/cursor/zed)
  - **Ignore management**:
    - `all`: Show all projects including ignored ones
    - `ignore-list`: Show currently ignored projects
    - `add-ignore`: Add a project to ignore list
    - `remove-ignore`: Remove a project from ignore list
  - See [ypm-open-spec.md](docs/development/ypm-open-spec.md) for details

### New Project Setup
- `/ypm-new` - Launch interactive project setup wizard

### Community Export
- `/ypm-export-community` - Export private repository to public community version
  - **Multi-language support**: Automatic language detection (Japanese/English)
  - **Interactive setup**: Configure private/public repositories, file exclusions, and commit sanitization
  - **Upstream safety**: Automatic repository verification to prevent mistakes
  - **Security scan**: TruffleHog integration for secret detection
  - See [global-export-system.md](docs/development/global-export-system.md) for details

**Usage**: Simply type the command in Claude Code, e.g., `/ypm-update`

**Note**: `/ypm-update` and similar operational commands do **not** use Git Flow. They update local files only (PROJECT_STATUS.md is `.gitignore`d). Git Flow is used **only for developing YPM itself** (adding features, fixing bugs).

---

## Project Bootstrap Assistant

YPM includes a comprehensive project setup assistant for launching new projects.

**What it does**:
- Guides you through project planning and requirements definition
- Creates proper directory structure with documentation
- Sets up Git workflow (Git Flow, Worktree support)
- Configures development environment (.gitignore, .claude/settings.json)
- Establishes documentation management rules (DDD, TDD, DRY principles)

**How to use**:

Simply run `/ypm-new` in Claude Code, or manually use the prompt:

1. Copy the contents of `project-bootstrap-prompt.md`
2. Paste into Claude Code
3. Follow the interactive wizard through 8 phases

See [project-bootstrap-prompt.md](project-bootstrap-prompt.md) for details.

---

## Configuration

Edit `~/.ypm/config.yml` to customize monitoring (created by `/ypm:ypm-setup`):

```yaml
monitor:
  directories:
    - /path/to/your/projects    # Directories to monitor

  patterns:
    - "proj_*/*"                # Project detection patterns
    - "my-apps/*"

  exclude:
    - old_projects/*            # Exclude patterns

editor:
  default: code                 # Default editor (code/cursor/zed)

classification:
  active_days: 7                # Consider active if updated within N days
  inactive_days: 30             # Consider inactive if no updates for N days
```

---

## Using YPM as a Private Fork

You can use YPM as a private fork to manage your personal projects while staying synchronized with the public version.

### Why Use a Private Fork?

- Keep your project-specific configurations (`config.yml`, `CLAUDE.md`) private
- Store sensitive project information securely
- Sync with upstream updates to get new features
- Export improvements back to the public repository

### Setting Up a Private Fork

1. **Create a private fork**:
   ```bash
   # Clone the public repository
   git clone https://github.com/signalcompose/YPM.git YPM-private
   cd YPM-private

   # Create your private repository on GitHub (set as private)
   gh repo create your-username/YPM-private --private --source=. --remote=origin

   # Add upstream remote
   git remote add upstream https://github.com/signalcompose/YPM.git
   ```

2. **Synchronize with upstream**:
   ```bash
   # Fetch latest changes from public version
   git fetch upstream
   git merge upstream/develop
   ```

3. **Customize for your environment**:
   - Edit `config.yml` with your project directories
   - Update `CLAUDE.md` with your workflow preferences
   - These files are excluded from community exports

For detailed private fork management, see `CLAUDE.md` in your fork.

---

## Contributing

Contributions to YPM are welcome!

- **Repository**: [signalcompose/YPM](https://github.com/signalcompose/YPM)
- **Bug reports & feature requests**: [GitHub Issues](https://github.com/signalcompose/YPM/issues)
- **Pull requests**: Please follow the Git Flow in `CLAUDE.md`

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Hiroshi Yamato / dropcontrol**

- Website: [hiroshiyamato.com](https://hiroshiyamato.com/) | [yamato.dev](https://yamato.dev/)
- X: [@yamato](https://x.com/yamato)
- GitHub: [dropcontrol](https://github.com/dropcontrol)

Powered by Claude Code

---

**Manage your projects, simplified.** 🚀
