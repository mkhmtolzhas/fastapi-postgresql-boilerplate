
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from .model.Post import PostModel
from .schemas import PostCreate, PostBase, PostUpdate


class PostService:
    @staticmethod
    async def create_post(session: AsyncSession, post: PostCreate):
        new_post = PostModel(title=post.title, content=post.content)
        session.add(new_post)
        await session.commit()

        return {
            "message": "Post created successfully",
            "data": post
        }
    
    @staticmethod
    async def get_posts(session: AsyncSession):
        stmt = select(PostModel)
        results = await session.execute(stmt)
        posts = results.scalars().all()
        print(posts[0].title)
        return {
            "message": "Posts retrieved successfully",
            "data": [PostBase.model_validate(post).model_dump() for post in posts]
        }
    
    @staticmethod
    async def get_post_by_id(session: AsyncSession, post_id: int):
        query = select(PostModel).where(PostModel.id == post_id)
        result = await session.execute(query)
        post = result.scalars().first()

        if not post:
            raise Exception("Post not found")
        
        return {
            "message": "Post retrieved successfully",
            "data": PostBase.model_validate(post).model_dump()
        }
    
    @staticmethod
    async def update_post(session: AsyncSession, post_id: int, updated_post: PostUpdate):
        post = await session.get(PostModel, post_id)

        if not post:
            return {"message": "Post not found"}
        
        for key, value in updated_post.model_dump(exclude_unset=True).items():
            setattr(post, key, value)

        await session.commit()
        await session.refresh(post)  # Загружаем актуальные данные из БД

        # ✅ Преобразуем ORM-объект в Pydantic-модель, избегая проблемы с greenlet
        post_dict = PostBase.model_validate(post, from_attributes=True).model_dump()

        return {"message": "Post updated successfully", "data": post_dict}


    

    @staticmethod
    async def delete_post(session: AsyncSession, post_id: int):
        post = await session.get(PostModel, post_id)

        if not post:
            return {"message": "Post not found"}
        
        await session.delete(post)
        await session.commit()
        return {"message": "Post deleted successfully"}
    

        
