from uuid import UUID
from datetime import date, datetime

from pydantic import BaseModel, EmailStr
from enum import StrEnum


class Gender(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class CreateUser(BaseModel):
    name: str
    email: EmailStr
    gender: Gender
    birthday: date


class UserInDB(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    gender: Gender
    birthday: date
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    name: str | None
    email: EmailStr | None
    gender: Gender | None
    birthday: date | None
