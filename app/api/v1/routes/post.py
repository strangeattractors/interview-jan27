from uuid import UUID

from fastapi import APIRouter

from app.database.dependencies import sessDep
from app.models.auth.dependencies import authDep, authDepLimit, authLoadDep
from app.models.post import Post

router = APIRouter(prefix="/post", tags=["Post"])

