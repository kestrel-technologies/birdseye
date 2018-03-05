import pytest

from birdseye import create_app, sessions


@pytest.fixture
def client():
    app = create_app({"TESTING": True, "SESSION_DB": ":memory:"})
    return app.test_client()


def test_healthz(client):
    assert client.get("/healthz").status_code == 200


def test_login_redirects_to_salesforce(client):
    resp = client.get("/login")
    assert resp.status_code == 302
    assert "/services/oauth2/authorize?" in resp.headers["Location"]


def test_callback_without_query_serves_bridge_page(client):
    resp = client.get("/oauth/callback")
    assert resp.status_code == 200
    assert b"callback.js" in resp.data


def test_callback_creates_session(client):
    resp = client.get("/oauth/callback?access_token=abc&instance_url=https://example.my.salesforce.com")
    assert resp.status_code == 302
    assert "/customer360?sid=" in resp.headers["Location"]


def test_customer360_requires_session(client):
    resp = client.get("/customer360")
    assert resp.status_code == 302
    assert resp.headers["Location"].endswith("/login")


def test_session_lookup(client):
    sid = sessions.create_session("tok", "https://example.my.salesforce.com", ttl_days=1)
    assert sessions.get_session(sid)["token"] == "tok"
    sessions.invalidate(sid)
    assert sessions.get_session(sid) is None
