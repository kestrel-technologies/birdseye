#!/bin/sh
# Birdseye entrypoint (gunicorn, 4 workers). Sessions persist in birdseye-sessions.db next to the app.
exec gunicorn --bind "0.0.0.0:${PORT:-8080}" --workers 4 --access-logfile - "birdseye:create_app()"
