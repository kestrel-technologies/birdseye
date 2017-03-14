"""Thin wrapper around simple-salesforce, logged in as the Birdseye integration user."""
import os
from urllib.parse import urlparse

from . import config as cfg

_client = None


def _domain():
    # https://<name>.my.salesforce.com -> "<name>.my"
    host = urlparse(cfg.SF_LOGIN_URL).hostname or "login.salesforce.com"
    return host[: -len(".salesforce.com")] if host.endswith(".salesforce.com") else "login"


def client():
    global _client
    if _client is None:
        from simple_salesforce import Salesforce
        _client = Salesforce(username=os.environ["SF_USERNAME"], password=os.environ["SF_PASSWORD"],
                             security_token=os.environ["SF_SECURITY_TOKEN"], domain=_domain(),
                             version=cfg.SF_API_VERSION)
    return _client


def query(soql):
    return client().query_all(soql).get("records", [])


def account(account_id):
    rows = query("SELECT Id, Name, Industry, BillingCity, BillingCountry, Owner.Name FROM Account "
                 "WHERE Id = '%s'" % account_id)
    return rows[0] if rows else None


def contacts(account_id):
    return query("SELECT Id, Name, Title, Email, Phone FROM Contact WHERE AccountId = '%s' "
                 "ORDER BY LastName" % account_id)


def open_opportunities(account_id):
    return query("SELECT Id, Name, StageName, Amount, CloseDate FROM Opportunity "
                 "WHERE AccountId = '%s' AND IsClosed = false ORDER BY CloseDate" % account_id)


def open_cases(account_id):
    return query("SELECT Id, CaseNumber, Subject, Status, Priority FROM Case "
                 "WHERE AccountId = '%s' AND IsClosed = false ORDER BY CreatedDate DESC" % account_id)


def search_accounts(term):
    term = term.replace("'", "")
    return query("SELECT Id, Name, Industry, BillingCountry FROM Account WHERE Name LIKE '%%%s%%' "
                 "ORDER BY Name LIMIT 50" % term)
