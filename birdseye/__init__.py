"""Birdseye: Skyward customer-360. One page per account: contacts, open opportunities, open cases."""
import logging

from flask import Flask, render_template, request

from . import config as cfg


def create_app(overrides=None):
    app = Flask(__name__)
    app.config.from_object(cfg)
    if overrides:
        app.config.update(overrides)
    logging.basicConfig(level=getattr(logging, cfg.LOG_LEVEL, logging.INFO),
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    from . import auth, customer360
    app.register_blueprint(auth.bp)
    app.register_blueprint(customer360.bp)

    @app.before_request
    def fragment_bridge():
        # The authorize redirect carries the token in the URL fragment, which the browser
        # does not send to the server; serve callback.js so it can come back with a query string.
        if request.path == "/oauth/callback" and not request.args:
            return render_template("callback.html")
        return None

    @app.route("/healthz")
    def healthz():
        return "ok"

    return app
