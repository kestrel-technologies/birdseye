# Birdseye runbook

## Deploy

1. Build the image from `Dockerfile` and push it to the Birdseye host's registry.
2. On the host: pull, restart the `birdseye` service, check `/healthz`.
3. Sessions live in `birdseye-sessions.db` next to the app; a restart does not sign anyone out.

## Integration login

Birdseye reads Salesforce as `svc.birdseye`. The login, password and security token are in
`birdseye/config.py`; the Salesforce side keeps the same login in the `SKY_Legacy_Integration_Config`
custom setting for the Apex sync. Changing the password means updating both and redeploying.

## Operations log

- 2017-03-06 · First deploy on the Austin app host (T. Lund).
- 2017-05-18 · Sign in with Salesforce enabled; users no longer share the team login.
- 2018-01-16 · Sessions extended to 30 days at Sales Ops' request (fewer sign-ins on the road).
- 2018-06-04 · Moved to the new Austin host; DNS `birdseye` updated.
- 2019-03-11 · Salesforce API version bumped; no code changes needed.
- 2019-11-04 · Integration login moved from host environment variables into `config.py`.
- 2020-05-11 · Runtime upgraded to Python 3.8 and Flask 1.1.
- 2021-04-12 · Skyward Data is now part of Kestrel. Birdseye stays up for Vantage Sales Ops.
- 2022-11-07 · Repointed to the Vantage production org (`kestrelvantage-prod`); repository mirrored to Roost.
- 2023-11-02 · Annual app attestation submitted (C. Marsh).
- 2024-06-28 · Deprecated after architecture review KSS-REV-0419; maintenance only.
- 2025-06-27 · C. Marsh has left; Sales Ops (P. Ramaswamy) keeps the host running.
- 2026-10-09 · External networks now see `ops/maintenance.html` (INC-0471).
