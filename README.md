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

## Configuration

Edit `config.yml` to customize monitoring:

```yaml
monitor:
  directories:
    - /path/to/your/projects    # Directories to monitor

  patterns:
    - "proj_*/*"                # Project detection patterns
    - "my-apps/*"

  exclude:
    - old_projects/*            # Exclude patterns

classification:
  active_days: 7                # Consider active if updated within N days
  inactive_days: 30             # Consider inactive if no updates for N days
```

---

## Contributing

Contributions are welcome!

- **Bug reports & feature requests**: [GitHub Issues](https://github.com/signalcompose/YPM/issues)
- **Pull requests**: Fork, create a feature branch, and submit a PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

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
