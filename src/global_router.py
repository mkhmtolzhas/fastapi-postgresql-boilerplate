from fastapi import APIRouter
from src.posts.router import router as post_router

router = APIRouter(prefix="/api/v1")

router.include_router(post_router, prefix="/post", tags=["post"])