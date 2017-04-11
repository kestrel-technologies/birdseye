"""Customer 360 views."""
from flask import Blueprint, abort, render_template, request, url_for

from . import sf_client

bp = Blueprint("customer360", __name__)


def link(endpoint, sid=None, **kw):
    return url_for(endpoint, **kw)


@bp.route("/")
@bp.route("/customer360")
def home():
    term = request.args.get("q", "").strip()
    accounts = sf_client.search_accounts(term) if term else []
    return render_template("search.html", sid=None, q=term, accounts=accounts, link=link)


@bp.route("/customer360/account/<account_id>")
def account(account_id):
    acct = sf_client.account(account_id)
    if acct is None:
        abort(404)
    return render_template(
        "account.html", sid=None, account=acct, link=link,
        contacts=sf_client.contacts(account_id),
        opportunities=sf_client.open_opportunities(account_id),
    )
