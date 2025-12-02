---
description: "Show next tasks for all projects in priority order"
---

Extract "next tasks" from `PROJECT_STATUS.md` and display in priority order.

**Display Format**:
- Project name
- Current Phase
- Next task
- Last update date

**Priority Order**:
1. Active projects (updated within 1 week)
2. Projects with high implementation progress
3. By Phase order

**Recommended Action**:
- Suggest the highest priority project
- Clarify the next task to work on

**CRITICAL: Reporting Guidelines**:
- Display "next task" as-is from PROJECT_STATUS.md
- DO NOT create new plans or features
- Include Issue number if GitHub Issues exist
- Add "(source unknown)" if information source is unclear
