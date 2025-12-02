<!-- Language Handling: Check ~/.ypm/config.yml for settings.language -->
<!-- If language is not "en", translate all output to that language -->

# YPM - TruffleHog Security Scan

Runs TruffleHog security scan on all projects managed by YPM.

## Overview

This command performs the following:
1. Run `python scripts/scan_projects.py` to get project list
2. Execute TruffleHog scan on each project
3. Display detected issues in a readable format

## Execution Steps

### STEP 1: Check TruffleHog Installation

```bash
which trufflehog
```

**If trufflehog is not installed**:
```
TruffleHog is not installed.

Installation:
brew install trufflehog

Please run this command again after installation.
```
→ **Abort processing**

### STEP 2: Execute Project Scan

```bash
python scripts/scan_projects.py
```

Read the scan result JSON and check `security_scan` information for each project.

### STEP 3: Display Scan Results

#### 3-1. Summary Display

```
## TruffleHog Security Scan Results

**Scan Date/Time**: 2025-11-11 10:30

**Summary**:
- Total Projects: 27
- Scanned: 27
- Issues Found: 1
- Clean: 26
```

#### 3-2. Projects with Issues

Display projects with detected issues first:

```
---

## Security Issues Detected

### project-name
- **Path**: /path/to/project
- **Branch**: main
- **Issues Found**: 6
- **Last Update**: 8 months ago
- **Recommended Actions**:
  1. Check details in project directory: `cd /path/to/project`
  2. Detailed TruffleHog scan: `trufflehog git file://. --json | jq`
  3. Remove detected secrets or clean history with git-filter-repo

---
```

#### 3-3. Clean Projects (Optional)

```
## Clean Projects (26)

No issues detected:
- Project1
- Project2
- Project3
- ... (22 more)
```

### STEP 4: Suggest Next Actions

```
## Recommended Next Actions

### If Issues Were Detected
1. Run detailed scan for each project
2. Review detected secrets
3. Rotate secrets or clean history as needed

### Regular Scanning
- Recommend running this command weekly or monthly
- Also run when adding new projects

### Individual Project Scanning
Use `/trufflehog-scan` within each project for individual scanning
```

---

## Output Examples

### No Issues Found

```
## TruffleHog Security Scan Results

**Scan Date/Time**: 2025-11-11 10:30

**Summary**:
- Total Projects: 27
- Scanned: 27
- Issues Found: 0
- Clean: 27

---

## All Projects Are Clean

No security issues were detected.
```

### Issues Found

Display in STEP 3 format above

---

## Important Notes

### 1. Scan Time

- May take time if there are many projects
- Maximum 30 second timeout per project

### 2. False Positives

TruffleHog performs pattern matching for secrets, so false positives are possible.
Always verify detected content.

### 3. History Scanning

TruffleHog scans the entire Git history.
Even if current code has no secrets, they will be detected if included in past commits.

### 4. Privacy

Scan results include project names and paths.
Following YPM's "no external exposure of project information" policy,
do not include these results in Git commits or PRs.

---

**Always display results to user after executing this command.**
