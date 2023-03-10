from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import Comment
from ...users.models import User
from . import schemas
from ...exceptions import ItemNotFound


async def get_comment(session: AsyncSession, news_id: UUID) -> Comment:
    result = await session.execute(select(Comment).where(Comment.id == news_id).limit(1))
    comment = result.scalar_one_or_none()
    if comment is None:
        raise ItemNotFound('comment with this id is not found')
    return comment


async def get_all_comment(session: AsyncSession, user_id: UUID) -> list[Comment]:
    result = await session.execute(select(User).where(User.id == user_id).limit(1))
    user = result.scalar_one_or_none()
    if user is None:
        raise ItemNotFound('user with this id is not found')
    result = await session.execute(select(Comment).where(Comment.user_id == user_id))
    comment = result.scalars()
    comment_list = list(comment)
    if comment is None:
        raise ItemNotFound('comment for this user is not found')
    return comment_list


async def create_comment(session: AsyncSession, data: schemas.CreateComment) -> Comment:
    comment = Comment(**data.dict())
    session.add(comment)
    await session.commit()
    await session.refresh(comment)
    return comment


async def update_comment(session: AsyncSession, car_id: UUID, data: schemas.UpdateComment) -> Comment:
    car = await get_comment(session, car_id)
    for key, value in data.dict(exclude_none=True).items():
        setattr(car, key, value)
    await session.commit()
    await session.refresh(car)
    return car


async def delete_comment(session: AsyncSession, news_id: UUID):
    comment = await get_comment(session, news_id)
    await session.delete(comment)
    await session.commit()
