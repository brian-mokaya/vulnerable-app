import logging

logger = logging.getLogger(__name__)

VALID_USERNAME = "demo"
VALID_PASSWORD = "ripple"


def authenticate(username: str, password: str) -> bool:
    if not username or not password:
        logger.warning("Login request failed: missing username or password")
        return False

    if username != VALID_USERNAME or password != VALID_PASSWORD:
        logger.warning("Login request failed: invalid credentials for user %s", username)
        return False

    return True
