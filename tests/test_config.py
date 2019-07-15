from birdseye import config


def test_login_url_is_my_domain():
    assert config.SF_LOGIN_URL.startswith("https://")
    assert config.SF_LOGIN_URL.endswith(".my.salesforce.com")


def test_callback_url_matches_route():
    assert config.OAUTH_CALLBACK_URL.endswith("/oauth/callback")


def test_api_version_is_string():
    assert isinstance(config.SF_API_VERSION, str)
