# Portfolio maintenance scripts

The live `index.html` is the rendered portfolio source. Maintenance is intentionally conservative: normal content edits are made directly, and the manual workflows only preserve the current V3 design rules instead of rebuilding the site from older visual generations.

## Current maintenance path

- `refine_portfolio_v3.py` — current V3 guardrail/refinement layer. It is idempotent and preserves the approved interaction, credential, profile-metadata, light-mode and navigation behaviour.
- `finalize_portfolio_identity.py` — narrow cleanup for remaining identity consistency, including NETDES ordinal cleanup and browser-theme details.
- `sync_resume_preview.py` — resume-only generator. The resume workflow always follows it with `finalize_portfolio_identity.py` and `refine_portfolio_v3.py` so resume maintenance cannot restore outdated site styling.
- `apply_portfolio_identity.py` — retained as the original V2-to-dossier migration/recovery script. It is not part of normal V3 maintenance and should not be run automatically.

## Safety rules

1. Normal content edits must not trigger a full portfolio rebuild.
2. Both GitHub Actions workflows are manual-only.
3. Do not chain historical polish scripts into a workflow.
4. For current visual maintenance, use the manual workflow or run `finalize_portfolio_identity.py` followed by `refine_portfolio_v3.py`.
5. Keep black/neutral surfaces dominant and use Engineering/CMU burgundy as restrained identity and interaction emphasis, not glow or decoration.
6. Preserve the authored engineering-dossier direction: technical evidence, project writing and real engineering artifacts should carry the identity.
7. Do not reintroduce numbered sections, terminal/HUD decoration, mouse spotlights, scanner effects, glow-heavy cards or generic AI-template styling.

## Legacy helpers

The remaining scripts are retained only for history or narrowly scoped recovery. Several represent older design generations and can reintroduce deprecated patterns if run directly. They are intentionally excluded from automatic and normal manual maintenance paths.
