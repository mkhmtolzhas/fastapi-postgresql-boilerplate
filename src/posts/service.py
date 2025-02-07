
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from .model.Post import PostModel
from .schemas import PostCreate


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
        return {
            "message": "Posts retrieved successfully",
            "data": posts
        }