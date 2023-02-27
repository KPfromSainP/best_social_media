from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from ...users.schemas import UserInDB
from ..news.schemas import NewsInDB


class CreateComment(BaseModel):
    text: str
    user_id: UUID
    news_id: UUID


class UpdateComment(BaseModel):
    text: str


class CommentInDB(BaseModel):
    id: UUID
    text: str
    user: UserInDB | None
    user_id: UUID | None
    news: NewsInDB | None
    news_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
