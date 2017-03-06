"""Birdseye: Skyward customer-360. One page per account: contacts, open opportunities, open cases."""
import logging

from flask import Flask

from . import config as cfg


def create_app(overrides=None):
    app = Flask(__name__)
    app.config.from_object(cfg)
    if overrides:
        app.config.update(overrides)
    logging.basicConfig(level=getattr(logging, cfg.LOG_LEVEL, logging.INFO),
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    from . import customer360
    app.register_blueprint(customer360.bp)

    @app.route("/healthz")
    def healthz():
        return "ok"

    return app
