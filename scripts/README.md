# Portfolio maintenance scripts

The live `index.html` is the rendered portfolio source. Maintenance is intentionally conservative: normal content edits are made directly, while the manual workflows preserve the approved identity and responsive behavior instead of rebuilding the site from older visual generations.

## Current maintenance path

Run the current layers in this order:

1. `finalize_portfolio_identity.py` — narrow cleanup for remaining identity consistency, including NETDES ordinal cleanup and browser-theme details.
2. `refine_portfolio_v3.py` — V3 identity/content guardrail. It preserves the approved interaction language, credentials, profile metadata, light-mode treatment and navigation decisions.
3. `refine_responsive_v4.py` — canonical responsive/input-capability layer. It is idempotent and translates the same interaction language across mouse, keyboard and touch while preserving the approved desktop design.

`sync_resume_preview.py` is the resume-only generator. The resume workflow always follows it with the three current maintenance layers above so resume work cannot restore older styling or remove mobile/touch behavior.

`apply_portfolio_identity.py` is retained only as the original V2-to-dossier migration/recovery script. It is not part of normal maintenance and must not be run automatically.

## Responsive V4 rules

- Mouse/trackpad enhancements live behind `(hover: hover) and (pointer: fine)` where appropriate.
- Touch devices receive restrained `:active` feedback rather than fake hover behavior.
- Keyboard `:focus-visible` remains part of the baseline accessibility system.
- Layout progressively adapts through the existing V4 breakpoints; do not create a separate mobile design.
- Keep interactive touch targets usable without making the visible UI oversized.
- Preserve the approved desktop hover behavior and the subtle burgundy-tinted light-mode surfaces.

## Safety rules

1. Normal content edits must not trigger a full portfolio rebuild.
2. Both GitHub Actions workflows are manual-only.
3. Do not chain historical polish scripts into a workflow.
4. For current maintenance, use the manual workflow or run `finalize_portfolio_identity.py`, then `refine_portfolio_v3.py`, then `refine_responsive_v4.py`.
5. Keep black/neutral surfaces dominant and use Engineering/CMU burgundy as restrained identity and interaction emphasis, not glow or decoration.
6. Preserve the authored engineering-dossier direction: technical evidence, project writing and real engineering artifacts should carry the identity.
7. Do not reintroduce numbered sections, terminal/HUD decoration, mouse spotlights, scanner effects, glow-heavy cards or generic AI-template styling.
8. Responsive work must not silently rewrite portfolio content, credentials or translations.

## Legacy helpers

The remaining scripts are retained only for history or narrowly scoped recovery. Several represent older design generations and can reintroduce deprecated patterns if run directly. They are intentionally excluded from automatic and normal manual maintenance paths.
