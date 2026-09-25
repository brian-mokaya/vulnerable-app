from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    database_url: str | None
    app_name: str = "Ripple Demo API"


def get_settings() -> Settings:
    return Settings(database_url=os.getenv("DATABASE_URL"))
