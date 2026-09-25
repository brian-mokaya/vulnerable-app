import os
import logging

logger = logging.getLogger(__name__)

# The application expects DATABASE_URL to be set in the environment.
# A later commit intentionally renames this to DB_URL to demonstrate a
# broken configuration — the health endpoint will then report "degraded".
DATABASE_URL: str | None = os.getenv("DATABASE_URL")

APP_SECRET_KEY: str = os.getenv("APP_SECRET_KEY", "dev-secret-change-me")
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

if DATABASE_URL is None:
    logger.warning(
        "DATABASE_URL is not set. "
        "The application will start but database connectivity will be unavailable. "
        "Set DATABASE_URL in your environment or .env file."
    )
