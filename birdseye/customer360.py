"""Customer 360 views. Every page carries ?sid= so links can be shared between Sales Ops and Support."""
from flask import Blueprint, abort, redirect, render_template, request, url_for

from . import sf_client
from .sessions import get_session

bp = Blueprint("customer360", __name__)


def _session_or_login():
    sess = get_session(request.args.get("sid"))
    if sess is None:
        return None, redirect("/login")
    return sess, None


def link(endpoint, sid, **kw):
    return url_for(endpoint, sid=sid, **kw)


@bp.route("/")
def index():
    return redirect("/login")


@bp.route("/customer360")
def home():
    sess, resp = _session_or_login()
    if resp:
        return resp
    term = request.args.get("q", "").strip()
    accounts = sf_client.search_accounts(term) if term else []
    return render_template("search.html", sid=sess["sid"], q=term, accounts=accounts, link=link)


@bp.route("/customer360/account/<account_id>")
def account(account_id):
    sess, resp = _session_or_login()
    if resp:
        return resp
    acct = sf_client.account(account_id)
    if acct is None:
        abort(404)
    return render_template(
        "account.html", sid=sess["sid"], account=acct, link=link,
        contacts=sf_client.contacts(account_id),
        opportunities=sf_client.open_opportunities(account_id),
    )
