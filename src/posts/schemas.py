from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(PostCreate):
    pass


    class Config:
        from_attributes = True
    

class PostBase(PostCreate):
    id: int


    class Config:
        from_attributes = True

    