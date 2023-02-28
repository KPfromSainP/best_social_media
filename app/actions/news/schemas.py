from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from ...users.schemas import UserInDB


class CreateNews(BaseModel):
    text: str
    user_id: UUID | None


class UpdateNews(BaseModel):
    text: str | None


class NewsInDB(BaseModel):
    id: UUID
    text: str
    user: UserInDB | None
    user_id: UUID | None
    created_at: datetime

    class Config:
        orm_mode = True
