<!-- Language Handling: Check ~/.ypm/config.yml for settings.language -->
<!-- If language is not "en", translate all output to that language -->

Extract "next tasks" from `PROJECT_STATUS.md` for each project and display them in priority order.

**Display Format**:
- Project name
- Current Phase
- Next task
- Last update date

**Priority Order**:
1. Active projects (updated within the last week)
2. Projects with higher implementation progress
3. Phase order

**Recommended Actions**:
- Suggest the highest priority project
- Clarify the next task to work on

**CRITICAL: Reporting Notes**:
- Display the "next tasks" as recorded in PROJECT_STATUS.md
- Do not create new plans or features
- If there are GitHub Issues, include the Issue numbers
- If the source is unclear, append "(source unknown)"
