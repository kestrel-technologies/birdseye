"""Session store (in-memory)."""
import secrets
import time

_sessions = {}


def create_session(token, instance_url, ttl_days=1):
    sid = secrets.token_hex(16)
    _sessions[sid] = (token, instance_url, time.time() + ttl_days * 86400)
    return sid


def get_session(sid):
    row = _sessions.get(sid) if sid else None
    if row is None or row[2] < time.time():
        return None
    return {"sid": sid, "token": row[0], "instance_url": row[1], "expires": row[2]}
