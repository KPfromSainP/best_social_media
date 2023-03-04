from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models import News
from ...users.models import User
from . import schemas
from ...exceptions import ItemNotFound


async def get_news(session: AsyncSession, news_id: UUID) -> News:
    result = await session.execute(select(News).where(News.id == news_id).limit(1))
    news = result.scalar_one_or_none()
    print(news)
    if news is None:
        raise ItemNotFound('news with this id is not found')
    return news


async def get_all_news(session: AsyncSession, user_id: UUID) -> list[News]:
    result = await session.execute(select(User).where(User.id == user_id).limit(1))
    user = result.scalar_one_or_none()
    if user is None:
        raise ItemNotFound('user with this id is not found')
    result = await session.execute(select(News).where(News.user_id == user_id))
    news = result.scalars()
    news_list = list(news)
    if news is None:
        raise ItemNotFound('news for this user is not found')
    return news_list


async def create_news(session: AsyncSession, data: schemas.CreateNews) -> News:
    news = News(**data.dict())
    session.add(news)
    await session.commit()
    await session.refresh(news)
    return news


async def delete_news(session: AsyncSession, news_id: UUID):
    news = await get_news(session, news_id)
    await session.delete(news)
    await session.commit()
