from fastapi import APIRouter

from app.services.users import list_users

router = APIRouter()


@router.get("/users")
def users() -> list[dict[str, str]]:
    return list_users()
