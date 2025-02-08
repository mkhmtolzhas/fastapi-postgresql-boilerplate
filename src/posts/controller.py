from .service import PostService
from .schemas import PostCreate, PostUpdate
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
        

    @staticmethod
    async def get_post_by_id(session: AsyncSession, post_id: int):
        try:
            return await PostService.get_post_by_id(session=session, post_id=post_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        
    @staticmethod
    async def update_post(session: AsyncSession, post_id: int, updated_post: PostUpdate):
        try:
            return await PostService.update_post(session=session, post_id=post_id, updated_post=updated_post)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    

    @staticmethod
    async def delete_post(session: AsyncSession, post_id: int):
        try:
            return await PostService.delete_post(session=session, post_id=post_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
