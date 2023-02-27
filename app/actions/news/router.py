from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas, service
from ...database import get_session

news = APIRouter(prefix='/news', tags=['news'])


@news.get('/{news_id}')
async def get_news_by_id(news_id: UUID, db: AsyncSession = Depends(get_session)) -> schemas.NewsInDB:
    return await service.get_news(db, news_id)


# @news.get('/{news_id}')
# async def get_all_news_by_id(news_id: UUID, db: AsyncSession = Depends(get_session)) -> List[schemas.NewsInDB]:
#     return await service.get_all_news(db, news_id)


@news.post('/')
async def create_news(data: schemas.CreateNews, db: AsyncSession = Depends(get_session)) -> schemas.NewsInDB:
    return await service.create_news(db, data)


@news.delete('/{news_id}')
async def delete_news(news_id: UUID, db: AsyncSession = Depends(get_session)):
    await service.delete_news(db, news_id)
    return {'detail': 'success'}
