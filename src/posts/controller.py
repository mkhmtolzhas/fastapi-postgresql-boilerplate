from .service import PostService
from .schemas import PostCreate
from fastapi import HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession

class PostController:
    @staticmethod
    async def get_all_posts(session: AsyncSession):
        try:
            return await PostService.get_posts(session=session)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @staticmethod
    async def create_post(session, post : PostCreate):
        try:
            return await PostService.create_post(session=session, post=post)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
