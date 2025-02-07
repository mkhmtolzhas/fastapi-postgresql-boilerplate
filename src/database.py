from typing import Annotated, AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.config import Config


engine = create_async_engine(Config.DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession)



async def get_session():
    async with async_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]