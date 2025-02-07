from fastapi import APIRouter
from src.database import SessionDep
from .controller import PostController
from .schemas import PostCreate

router = APIRouter()


@router.get("/")
async def get_all_posts(session: SessionDep):
    return await PostController.get_all_posts(session)


@router.post("/")
async def create_post(session: SessionDep, post : PostCreate):
    return await PostController.create_post(session=session, post=post)
