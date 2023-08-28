from fastapi import APIRouter

from . import query
from . import command

router = APIRouter()

router.include_router(query.router)
router.include_router(command.router)

__all__ = ["router"]
