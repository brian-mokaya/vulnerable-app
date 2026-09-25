import logging

from app.config import get_settings

logger = logging.getLogger(__name__)


def get_database_status() -> tuple[str, str]:
    settings = get_settings()
    if not settings.database_url:
        logger.warning("Database configuration missing: DATABASE_URL is not set")
        return "degraded", "unavailable"

    return "healthy", "connected"
