# Birdseye

Birdseye is the Skyward customer-360 web app: one page per account with contacts, open
opportunities and open cases, read from Salesforce through the `svc.birdseye` integration user.
<img src="birdseye/static/logo-skyward.svg" alt="Skyward" height="22" style="background:#6b7a2a;padding:4px">

## What it does

| Page | URL | Data |
|---|---|---|
| Account search | `/customer360?q=<name>` | Account name, industry, country |
| Customer 360 | `/customer360/account/<id>` | Account, contacts, open opportunities, open cases |
## Running locally

```sh
python3.8 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
FLASK_APP="birdseye:create_app()" flask run --port 8080
```

## Tests

```sh
pip install pytest flake8
flake8 birdseye tests && pytest -q
```
