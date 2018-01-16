"""Session store: in-memory cache in front of a small sqlite table (survives gunicorn restarts)."""
import secrets
import sqlite3
import threading
import time

_lock = threading.Lock()
_cache = {}
_db_path = ":memory:"
_conn = None


def init_store(path):
    global _db_path, _conn
    _db_path = path
    _conn = sqlite3.connect(_db_path, check_same_thread=False)
    _conn.execute("CREATE TABLE IF NOT EXISTS sessions (sid TEXT PRIMARY KEY, token TEXT, "
                  "instance_url TEXT, expires REAL)")
    _conn.commit()
    _cache.clear()


def create_session(token, instance_url, ttl_days=30):
    sid = secrets.token_hex(16)
    expires = time.time() + ttl_days * 86400
    with _lock:
        _cache[sid] = (token, instance_url, expires)
        if _conn is not None:
            _conn.execute("INSERT OR REPLACE INTO sessions VALUES (?, ?, ?, ?)", (sid, token, instance_url, expires))
            _conn.commit()
    return sid


def get_session(sid):
    if not sid:
        return None
    with _lock:
        row = _cache.get(sid)
        if row is None and _conn is not None:
            hit = _conn.execute("SELECT token, instance_url, expires FROM sessions WHERE sid = ?", (sid,)).fetchone()
            row = tuple(hit) if hit else None
            if row:
                _cache[sid] = row
    if row is None or row[2] < time.time():
        return None
    return {"sid": sid, "token": row[0], "instance_url": row[1], "expires": row[2]}


def invalidate(sid):
    with _lock:
        _cache.pop(sid, None)
        if _conn is not None:
            _conn.execute("DELETE FROM sessions WHERE sid = ?", (sid,))
            _conn.commit()
