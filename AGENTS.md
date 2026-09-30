# AGENTS.md

This repository is expected to satisfy the see.io deployment contract before it can go live.

Contract:

1. A Dockerfile at the project root must build an image serving plain HTTP on port 8080.
2. A root-level `seeio.json` file must exist with the shape:
   {"name": "<human site name>", "healthcheck": "/<path>"}
3. The app must create and use `/data` at runtime. Anything stateful must live under `/data`.
4. The healthcheck path must return HTTP 200 immediately when the container starts.

Operational loop:

- Always pull before changes: `git pull --rebase`
- Commit changes with `git add -A && git commit -m "<what changed>"`
- Push to `main` only: `git push origin main`
- Poll the site status endpoint until it is `live` or `deploy_failed`
- If `deploy_failed`, fix the root cause and push again; never rewrite history

This file is intentionally kept at the repository root so future build sessions can read the same deployment contract and status expectations.
