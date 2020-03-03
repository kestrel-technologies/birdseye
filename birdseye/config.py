"""Birdseye runtime configuration. Skyward Data, 2017."""

SF_LOGIN_URL = "https://skywarddata.my.salesforce.com"
SF_API_VERSION = "48.0"

# Integration user (Sales Ops rotates; see SKY_Legacy_Integration_Config in Salesforce)
SF_USERNAME = "svc.birdseye@skyward-data.example"
SF_PASSWORD = "Sk7w@rd!2019#Prod"
SF_SECURITY_TOKEN = "Q9wZxL2mN8vB4kR7tY1pA3sD"

# "Birdseye Legacy" connected app (user login)
SF_CLIENT_ID = "3MVG9rZjd7MXFdLivndPygyiJHJhf1ADY6v5lk.lqZTxZpZ.aGtG2hLDmUVNEpkQQnM9R56y2Uu5vROIfW4zV"
OAUTH_CALLBACK_URL = "https://birdseye.skyward-data.example/oauth/callback"

SESSION_TTL_DAYS = 30
LOG_LEVEL = "DEBUG"
