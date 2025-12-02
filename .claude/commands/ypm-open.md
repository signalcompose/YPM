<!-- Language Handling: Check ~/.ypm/config.yml for settings.language -->
<!-- If language is not "en", translate all output to that language -->

# YPM - Open Project in Editor

Opens projects managed by YPM in a specified editor.

## Subcommands

- **(no arguments)**: Select from list (excluding ignored) and open in default editor
- `<project_name> [editor_name]`: Open project in specified editor
- `all`: Select from all projects including ignored
- `ignore-list`: Show projects in ignore list
- `add-ignore`: Add project to ignore list
- `remove-ignore`: Remove project from ignore list
- `--editor [editor_name]`: Show/set default editor

## Usage Examples

```
/ypm-open                    # Normal mode (default editor)
/ypm-open myproject          # Open myproject in default editor
/ypm-open myproject cursor   # Open myproject in Cursor
/ypm-open myproject terminal # Open myproject in Terminal.app
/ypm-open all                # Full display mode
/ypm-open --editor           # Show current default editor
/ypm-open --editor cursor    # Set default to Cursor
/ypm-open ignore-list        # Show ignore list
/ypm-open add-ignore         # Add to ignore
/ypm-open remove-ignore      # Remove from ignore
```

**Supported Editors**: `code` (VS Code), `cursor` (Cursor), `zed` (Zed), `terminal` (Terminal.app)

---

## Execution Steps

### Common STEP: Check Arguments

Check arguments and branch to corresponding mode:
- No arguments → **Mode 1: Normal Mode**
- `<project_name> [editor_name]` → **Mode 1: Normal Mode** (direct project specification)
- `all` → **Mode 2: Full Display Mode**
- `ignore-list` → **Mode 3: Ignore List**
- `add-ignore` → **Mode 4: Add Ignore**
- `remove-ignore` → **Mode 5: Remove Ignore**
- `--editor [editor_name]` → **Mode 6: Editor Settings**

---

## Mode 1: Normal Mode (no arguments or project name specified)

### STEP 1: Check config.yml and Editor CLI

#### 1-1. Get default editor from config.yml

```bash
# Read config.yml
# Get editor.default value (e.g., code, cursor, zed)
```

#### 1-2. Override editor if second argument exists

- If second argument (`cursor`, `code`, `zed`, etc.) is specified, use that editor
- If no second argument, use default from config.yml

#### 1-3. Check Editor CLI

**For editors other than Terminal.app**:

```bash
which <editor_name>
```

**If result is empty**:
```
Editor <editor_name> CLI not found.

Please install the <editor_name> CLI.

[VS Code (code)]
1. Open VS Code
2. Command Palette (Cmd+Shift+P)
3. Run "Shell Command: Install 'code' command in PATH"

[Cursor (cursor)]
1. Open Cursor
2. Command Palette (Cmd+Shift+P)
3. Run "Shell Command: Install 'cursor' command in PATH"

[Zed (zed)]
1. Open Zed
2. Command Palette (Cmd+Shift+P)
3. Run "zed: Install CLI"

Please run this command again after installation.
```
→ **Abort processing**

**For Terminal.app**:
- CLI check not needed (built into macOS)
- Proceed to next STEP

### STEP 2: Read PROJECT_STATUS.md and config.yml

```bash
# Use Read tool to read PROJECT_STATUS.md
# Use Read tool to read config.yml
```

**If PROJECT_STATUS.md does not exist**:
```
PROJECT_STATUS.md not found.

Please run /ypm-update first to scan projects.
```
→ **Abort processing**

### STEP 3: Extract Project List and Exclusions

#### 3-1. Extract from PROJECT_STATUS.md

1. **Active Projects** (`## Active Projects` section)
2. **Developing Projects** (`## Developing` section)
3. **Dormant Projects** (`## Dormant` section)

**Extraction Rules**:
- Get project name from `### ProjectName` line
- Get brief description from `- **Overview**: ...`
- Get progress from `- **Implementation Progress**: XX%`
- Extract project path from `- **Documentation**: [...]`
  - Example: `[CLAUDE.md](/path/to/project/CLAUDE.md)`
  - → Project path: `/path/to/project`

#### 3-2. Exclude Git Worktrees

Exclude projects that match **any** of the following:
- Project name ends with `-main`
- Project name ends with `-develop`
- Overview contains "worktree"

#### 3-3. Exclude ignore_in_open (Normal Mode Only)

Exclude projects in the `monitor.ignore_in_open` list in config.yml.

### STEP 4: Display Numbered List

```
## Available Projects (12)

### Active (Updated within 1 week)
1. ProjectA - Description (95%)
2. ProjectB - Description (100%)
3. ProjectC - Description (35%)
...

### Developing (Updated within 1 month)
12. ProjectX - Description (0%)
...

* Hidden: 2 (show all: /ypm-open all)

Enter number or project name:
```

### STEP 5: User Input Processing

**Input Patterns**:

#### 5-1. Number Input (e.g., `3`)
- Select project with that number → Go to STEP 6

#### 5-2. Project Name Input (e.g., `proj`)
- Case-insensitive partial match search
- **1 match**: Select that project → Go to STEP 6
- **Multiple matches**:
  ```
  Multiple projects matched:

  1. ProjectA
  2. ProjectB

  Enter number:
  ```
  → Wait for number input again → Go to STEP 6

- **0 matches**:
  ```
  Project "xxx" not found.

  Please specify exact project name or number.
  ```
  → **Abort processing**

### STEP 6: Open Project in Editor

#### 6-1. For Editors Other Than Terminal.app

**Important**: Launch editor with environment variables cleared. This ensures each project's `.node-version` etc. are read correctly.

```bash
env -u NODENV_VERSION -u NODENV_DIR -u RBENV_VERSION -u PYENV_VERSION <editor_name> /path/to/project
```

**Environment Variables to Clear**:
- `NODENV_VERSION` - Node.js version (nodenv)
- `NODENV_DIR` - nodenv directory
- `RBENV_VERSION` - Ruby version (rbenv)
- `PYENV_VERSION` - Python version (pyenv)

#### 6-2. For Terminal.app

**Important**: Reinitialize shell after changing directory to set environment variables correctly.

```bash
osascript -e 'tell application "Terminal" to do script "cd '"$PROJECT_PATH"' && exec $SHELL"'
```

#### 6-3. Success Message

**For editors other than Terminal.app**:
```
Opened "ProjectName" in <EditorDisplayName>.

Project path: /path/to/project
Editor: <EditorDisplayName> (<editor_name>)

* Launched with environment variables (NODENV_VERSION, etc.) cleared.
Project config files (.node-version, etc.) will be read correctly.
```

**For Terminal.app**:
```
Opened "ProjectName" in Terminal.app.

Project path: /path/to/project
Editor: Terminal.app (terminal)

* Shell reinitialized after moving to project directory.
Project config files (.node-version, etc.) will be read correctly.
```

**Editor Display Name Mapping**:
- `code` → "VS Code"
- `cursor` → "Cursor"
- `zed` → "Zed"
- `terminal` → "Terminal.app"

**Failure Message**:
```
Failed to launch <EditorDisplayName>.

Error: <error_message>

Please run the following command manually:
env -u NODENV_VERSION -u NODENV_DIR -u RBENV_VERSION -u PYENV_VERSION <editor_name> /path/to/project
```

---

## Mode 2: Full Display Mode (`/ypm-open all`)

### Processing

**STEP 1-2**: Same as Mode 1

**STEP 3**: Project Extraction
- Exclude worktrees
- **Do not exclude ignore_in_open** (this is the difference from Normal Mode)

**STEP 4**: Display numbered list (including ignored)

```
## Available Projects (All 16)

### Active
1-11. (same as Normal Mode)

### Developing
12-14. (same as Normal Mode)

### Dormant/Other (in ignore list)
15. ProjectY - Description (dormant)
16. ProjectZ - Description (legacy, complete)

Enter number or project name:
```

**STEP 5-6**: Same as Mode 1

---

## Mode 3: Ignore List (`/ypm-open ignore-list`)

### Processing

```bash
# Read config.yml
# Extract monitor.ignore_in_open section
```

**Display**:
```
## Projects in Ignore List

1. project-a
2. project-b

Remove: /ypm-open remove-ignore
Add: /ypm-open add-ignore
```

**If ignore_in_open is empty**:
```
No projects currently in ignore list.

Add: /ypm-open add-ignore
```

---

## Mode 4: Add Ignore (`/ypm-open add-ignore`)

### STEP 1-3: Same as Mode 1 (Normal Mode)

### STEP 4: Display Project List

```
## Select project to add to ignore

Currently displayed projects (12):
1. ProjectA
2. ProjectB
...

Enter number or project name:
```

### STEP 5: Project Selection (same as Mode 1)

### STEP 6: Add to config.yml

Add selected project name to `monitor.ignore_in_open` list.

```yaml
monitor:
  ignore_in_open:
    - project-a
    - project-b
    - project-c  # added
```

**Success Message**:
```
Added "project-c" to ignore list.

Updated config.yml:
  monitor.ignore_in_open:
    - project-a
    - project-b
    - project-c

This project will not appear in /ypm-open from next time.
Show all: /ypm-open all
```

---

## Mode 5: Remove Ignore (`/ypm-open remove-ignore`)

### STEP 1: Read config.yml

```bash
# Read config.yml
# Extract monitor.ignore_in_open section
```

**If ignore_in_open is empty**:
```
No projects currently in ignore list.

Add: /ypm-open add-ignore
```
→ **Abort processing**

### STEP 2: Display Ignore List

```
## Select project to remove from ignore

1. project-a
2. project-b
3. project-c

Enter number or project name:
```

### STEP 3: Project Selection

Select by number or name (same logic as Mode 1 STEP 5)

### STEP 4: Remove from config.yml

Remove selected project name from `monitor.ignore_in_open` list.

```yaml
monitor:
  ignore_in_open:
    - project-a
    - project-b
    # project-c removed
```

**Success Message**:
```
Removed "project-c" from ignore list.

Updated config.yml:
  monitor.ignore_in_open:
    - project-a
    - project-b

This project will appear in /ypm-open from next time.
```

---

## Mode 6: Editor Settings (`/ypm-open --editor [editor_name]`)

### STEP 1: Check Arguments

#### No argument (`/ypm-open --editor`)

Display current default editor.

```bash
# Read config.yml
# Get editor.default value
```

**Display Message**:
```
Current Default Editor

Editor: VS Code (code)

Change: /ypm-open --editor <editor_name>
Supported: code (VS Code), cursor (Cursor), zed (Zed), terminal (Terminal.app)
```

#### With argument (`/ypm-open --editor cursor`)

Change default editor.

### STEP 2: Validate Editor Name

Check if specified editor name is supported.

**Supported Editors**:
- `code` - VS Code
- `cursor` - Cursor
- `zed` - Zed
- `terminal` - Terminal.app

**If not supported**:
```
Unsupported editor: "xxx"

Supported editors:
- code (VS Code)
- cursor (Cursor)
- zed (Zed)
- terminal (Terminal.app)

Example: /ypm-open --editor cursor
```
→ **Abort processing**

### STEP 3: Update config.yml

Change `editor.default` value to specified editor name.

```yaml
# Before
editor:
  default: code

# After
editor:
  default: cursor
```

### STEP 4: Success Message

```
Default editor changed

Before: VS Code (code)
After: Cursor (cursor)

Updated config.yml:
  editor.default: cursor

Cursor will be used for /ypm-open from next time.
```

---

## Important Notes

### 1. Git Worktree Exclusion

Git worktrees (e.g., `ProjectA-main`, `ProjectB-develop`) are **automatically excluded in all modes**. These are for review purposes, not development, so they are not included in selections.

### 2. Difference Between ignore and exclude

- **exclude**: Completely excluded from scanning (not shown in PROJECT_STATUS.md)
- **ignore_in_open**: Scanned but hidden by default in ypm-open (visible with `all`)

### 3. Saving config.yml

When adding/removing from ignore or changing editor settings, **always save** the config.yml file. Use the Write tool.

### 4. Updating PROJECT_STATUS.md

If the project list is outdated, run `/ypm-update` first.

### 5. Editor CLI Installation

If each editor's CLI is not installed, you cannot open projects. Installation instructions are shown in STEP 1.

---

## Error Handling

| Error | Action |
|-------|--------|
| Editor CLI not found | Show installation instructions and abort |
| Unsupported editor | Show supported editor list and abort |
| PROJECT_STATUS.md not found | Prompt to run `/ypm-update` and abort |
| config.yml not found | Show error message and abort |
| Project not found | Show error message and abort |
| Multiple matches | Re-display candidates with numbers |
| Editor launch failure | Show error message and manual command |

---

## Specification Document

See the following for detailed specifications:
- **[docs/development/ypm-open-spec.md](../../docs/development/ypm-open-spec.md)**

---

**Always display success/failure message to user after executing this command.**
