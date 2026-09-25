from fastapi import APIRouter

from app.services.database import get_database_status

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    status, database = get_database_status()
    return {"status": status, "database": database}
