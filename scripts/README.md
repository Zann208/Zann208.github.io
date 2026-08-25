# Portfolio maintenance scripts

The portfolio now has one canonical visual maintenance path:

- `apply_portfolio_identity.py` — source of truth for the homepage and NETDES visual identity.
- `sync_resume_preview.py` — resume-only generator. The resume workflow always follows it with `apply_portfolio_identity.py` so resume maintenance cannot restore legacy site styling.

## Safety rules

1. Normal content edits should be made directly and must not trigger a full rebuild.
2. Both GitHub Actions workflows are manual-only.
3. Do not chain the historical polish scripts into a workflow.
4. If the portfolio identity needs to be reapplied, use `apply_portfolio_identity.py` only.
5. Keep black/neutral surfaces dominant and use Engineering/CMU burgundy as restrained identity emphasis, not glow or decoration.
6. Prefer technical evidence, project writing and real engineering artifacts over terminal/HUD/AI-template decoration.

## Legacy helpers

The other scripts in this folder are retained only for history or narrowly scoped recovery. Several of them represent older design generations and can reintroduce deprecated patterns if run directly. They are intentionally not part of any automatic workflow.
