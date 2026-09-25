from __future__ import annotations

from contextlib import asynccontextmanager
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from fastapi import FastAPI

from app.config import get_settings
from app.routes.auth import router as auth_router
from app.routes.health import router as health_router
from app.routes.users import router as users_router
from app.services.database import get_database_status

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"


def configure_logging() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    has_stream_handler = any(
        isinstance(handler, logging.StreamHandler)
        and not isinstance(handler, RotatingFileHandler)
        for handler in root_logger.handlers
    )
    has_file_handler = any(
        isinstance(handler, RotatingFileHandler)
        and getattr(handler, "baseFilename", None) == str(LOG_FILE)
        for handler in root_logger.handlers
    )

    if not has_stream_handler:
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    if not has_file_handler:
        file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=1)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    logger.info("Ripple Demo API starting")
    if settings.database_url:
        logger.info("Database configuration detected")
    else:
        logger.warning("Database configuration missing: DATABASE_URL is not set")

    status, database = get_database_status()
    logger.info("Startup health snapshot: status=%s database=%s", status, database)
    yield


app = FastAPI(title="Ripple Demo API", lifespan=lifespan)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Ripple demo API is running"}
