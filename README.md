# Birdseye

> **DEPRECATED (2024-06-28).** Birdseye is scheduled for decommission (KSS-REV-0419, target Q3 2024).
> Do not add features. Sales Ops and Support L2 continue to use it until a replacement is available.
> Owner: Skyward Sales Ops (legacy). Questions: Vantage Business Systems.

Birdseye is the Skyward customer-360 web app: one page per account with contacts, open
opportunities and open cases, read from Salesforce through the `svc.birdseye` integration user.
Sign in with your Salesforce account (the "Birdseye Legacy" connected app).

<img src="birdseye/static/logo-skyward.svg" alt="Skyward" height="22" style="background:#6b7a2a;padding:4px">

## What it does

| Page | URL | Data |
|---|---|---|
| Sign in | `/login` | Redirects to Salesforce; the "Birdseye Legacy" connected app signs you in |
| Account search | `/customer360?q=<name>` | Account name, industry, country |
| Customer 360 | `/customer360/account/<id>` | Account, contacts, open opportunities, open cases |

Every page link carries the session id (`?sid=...`) so a page can be bookmarked or handed to a
colleague on the same team. Sessions last 30 days (`SESSION_TTL_DAYS`).

## Running locally

```sh
python3.8 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
FLASK_APP="birdseye:create_app()" flask run --port 8080
```

Production runs `run.sh` (gunicorn) in the container built from `Dockerfile`.
## Configuration

`birdseye/config.py` holds the Salesforce login URL (`kestrelvantage-prod` My Domain since 2022-11),
the API version, the integration user and the connected app's client id. Sales Ops rotates the
integration login; see the `SKY_Legacy_Integration_Config` custom setting in Salesforce.

## Tests

```sh
pip install pytest flake8
flake8 birdseye tests && pytest -q
```

## History

| Year | |
|---|---|
| 2017 | Built by Skyward Sales Ops engineering (T. Lund) |
| 2019 | Integration login moved into `config.py` |
| 2021 | Skyward Data acquired by Kestrel; Birdseye kept running for Vantage Sales Ops |
| 2022 | Repointed to the Vantage production org; repository mirrored to Roost |
| 2024 | Architecture review KSS-REV-0419; deprecated |

---

Kestrel Technologies is a fictional company created for an educational workshop. Nothing in this repository is a real credential, person or product. Mirrored from Roost by `roost-mirror`; CL metadata is preserved in commit trailers (`Roost-CL:`, `Reviewed-by:`).
