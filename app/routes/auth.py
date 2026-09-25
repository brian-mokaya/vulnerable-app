import logging

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services.auth import authenticate

logger = logging.getLogger(__name__)
router = APIRouter()


class LoginRequest(BaseModel):
    username: str | None = Field(default=None)
    password: str | None = Field(default=None)


@router.post("/login")
def login(payload: LoginRequest) -> dict[str, str]:
    username = payload.username or ""
    password = payload.password or ""

    if not authenticate(username, password):
        logger.warning("Login request failed for user: %s", payload.username or "unknown")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    return {"message": "login successful", "user": username}
