# Detailed Migration Notes — Iteration 1

## Guidance & Observations
- Agents-SDK: includes a `compat` namespace; suitable for stepwise migration and preserving older APIs.
- core-teams.net: ships a `Compat` package; use it to bridge newer core behaviors with legacy consumers.
- teams.net: provides a BotBuilder plugin — useful for migration of BotBuilder-based integrations.

## Migration Checklist
- Inventory public surface area (controllers, activity models, middleware).
- Map equivalent types across SDKs (Activity, TurnContext, Middleware interfaces).
- Identify serialization/contract differences and versioned models.
- Create compatibility adapters where direct API parity is missing.

## Actionable Items
- Automated: run reflection-based scans to map types and public API names across assemblies.
- Manual: review middleware pipeline differences and adapt ordering/registration.
