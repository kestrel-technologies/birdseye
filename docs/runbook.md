# Birdseye runbook

## Deploy

1. Build the image from `Dockerfile` and push it to the Birdseye host's registry.
2. On the host: pull, restart the `birdseye` service, check `/healthz`.
3. Sessions live in `birdseye-sessions.db` next to the app; a restart does not sign anyone out.

## Operations log

- 2017-03-06 · First deploy on the Austin app host (T. Lund).
- 2017-05-18 · Sign in with Salesforce enabled; users no longer share the team login.
- 2018-01-16 · Sessions extended to 30 days at Sales Ops' request (fewer sign-ins on the road).
- 2018-06-04 · Moved to the new Austin host; DNS `birdseye` updated.
