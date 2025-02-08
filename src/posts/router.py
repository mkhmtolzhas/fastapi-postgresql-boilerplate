from fastapi import APIRouter
from src.database import SessionDep
from .controller import PostController
from .schemas import PostCreate, PostUpdate

router = APIRouter()


@router.get("/")
async def get_all_posts(session: SessionDep):
    return await PostController.get_all_posts(session=session)


@router.post("/")
async def create_post(session: SessionDep, post : PostCreate):
    return await PostController.create_post(session=session, post=post)


@router.get("/{post_id}")
async def get_post_by_id(session: SessionDep, post_id: int):
    return await PostController.get_post_by_id(session=session, post_id=post_id)


@router.put("/{post_id}")
async def update_post(session: SessionDep, post_id: int, post: PostUpdate):
    return await PostController.update_post(session=session, post_id=post_id, updated_post=post)


@router.delete("/{post_id}")
async def delete_post(session: SessionDep, post_id: int):
    return await PostController.delete_post(session=session, post_id=post_id)
