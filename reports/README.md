# Reports — How to finish drafts

This folder contains draft reports and supporting notes created as iteration 1.

Files:
- `draft_report_iteration1.md` — high-level draft report
- `detailed_analysis/migration_notes.md` — migration-focused notes and checklist

Next steps to complete the report:
1. Scan the target library folders to collect concrete API lists and LOC metrics. Suggested tools: `cloc`, `git ls-files`, or a small .NET reflection script.
2. Populate `reports/charts/` with generated charts (e.g., `code-lines-by-repo.png`).
3. Update `draft_report_iteration1.md` with exact API names and metric visuals.

Example metric commands:
```bash
# count lines in a folder
cloc botbuilder-dotnet/libraries agents-for-net/src/libraries teams.net/Libraries core-teams.net/core/src --csv --out=reports/metrics/cloc.csv
```
