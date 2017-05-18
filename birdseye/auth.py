import logging
from urllib.parse import urlencode
from flask import Blueprint, redirect, request
from . import config as cfg
from .sessions import create_session

logger = logging.getLogger("birdseye.auth")
bp = Blueprint("auth", __name__)


@bp.route("/login")
def login():
    # Salesforce user-agent flow: the token comes back in the URL fragment,
    # callback.js forwards it to /oauth/callback as a query parameter.
    params = {
        "response_type": "token",
        "client_id": cfg.SF_CLIENT_ID,
        "redirect_uri": cfg.OAUTH_CALLBACK_URL,
    }
    return redirect(f"{cfg.SF_LOGIN_URL}/services/oauth2/authorize?{urlencode(params)}")


@bp.route("/oauth/callback")
def oauth_callback():
    token = request.args.get("access_token")
    instance_url = request.args.get("instance_url", cfg.SF_LOGIN_URL)
    logger.debug(f"token={token}")
    if not token:
        return "Login failed", 401
    sid = create_session(token, instance_url, ttl_days=cfg.SESSION_TTL_DAYS)
    return redirect(f"/customer360?sid={sid}")
