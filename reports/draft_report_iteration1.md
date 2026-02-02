# SDKs Comparison — Draft Report (Iteration 1)

## Executive Summary
- Purpose: Provide a baseline comparison and migration-focused evaluation for the four target SDKs specified in AGENTS.md. 🎯
- Scope: `botbuilder-dotnet` (libraries), `agents-for-net/src/libraries`, `teams.net/Libraries`, `core-teams.net/core/src`.
- Outcome: High-level feature comparison, code metrics placeholders, quality evaluation, and migration effort guidance.

## Feature Comparison
- Approach: list major surface-area features for each SDK, call out unique/overlapping functionality, and highlight migration-relevant APIs.
- Presentation: include emoji markers for clarity (✅ supported, ⚠️ partial/compat, ❌ missing).

| Feature Area | botbuilder-dotnet | agents-for-net | teams.net | core-teams.net |
|---|---:|---:|---:|---:|
| Core bot runtime | ✅ | ⚠️ | ⚠️ | ⚠️ |
| Activity model | ✅ | ✅ | ✅ | ✅ |
| Plugin/Extensibility | ✅ | ✅ | ✅ | ✅ |
| Compat/legacy APIs | ⚠️ | ✅ (compat) | ⚠️ (BotBuilder plugin) | ✅ (Compat package) |

> Note: Expand the table with concrete API names after scanning the libraries (next step).

## Code Metrics (placeholders)
- Summary metrics to compute: Lines of code, language breakdown, number of packages/projects, test coverage indicators.
- Chart placeholders:
  - `charts/code-lines-by-repo.png` — LOC comparison 📊
  - `charts/language-breakdown.png` — language pie chart 🥧

## Quality Evaluation
- Criteria: test coverage, CI status, security advisories, API stability, docs completeness.
- High-level pass/fail markers and rationale for each SDK.

## Migration Effort
- Focus: migration strategies and effort estimates for moving between SDKs or modernizing code.
- Key guidance:
  - Prefer migration paths leveraging compat namespaces/packages where available (Agents-SDK `compat`, core-teams.net `Compat`, teams.net BotBuilder plugin).
  - Inventory breaking changes: model shape differences, middleware patterns, serialization contracts.

## Next steps
- Run automated scans to populate metrics and expand the Feature Comparison with concrete API references.
- Produce charts and move data to `reports/detailed_analysis/`.

---
Generated as draft — iteration 1.
