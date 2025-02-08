from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base



class PostModel(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] 
    content: Mapped[str]


