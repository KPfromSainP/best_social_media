from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas, service
from ...database import get_session

comments = APIRouter(prefix='/comments', tags=['comments'])


@comments.get('/{comment_id}')
async def get_comment_by_id(comment_id: UUID, db: AsyncSession = Depends(get_session)) -> schemas.CommentInDB:
    return await service.get_comment(db, comment_id)


@comments.get('/get_all_comments/{user_id}')
async def get_all_comment_by_id(user_id: UUID, db: AsyncSession = Depends(get_session)) -> schemas.CommentsInDbForUser:
    return schemas.CommentsInDbForUser(comments=await service.get_all_comment(db, user_id))


@comments.post('/')
async def create_comment(data: schemas.CreateComment, db: AsyncSession = Depends(get_session)) -> schemas.CommentInDB:
    return await service.create_comment(db, data)


@comments.put('/{comment_id}')
async def change_car_info(comment_id: UUID, data: schemas.UpdateComment,
                          db: AsyncSession = Depends(get_session)) -> schemas.CommentInDB:
    return await service.update_comment(db, comment_id, data)


@comments.delete('/{comment_id}')
async def delete_comment(comment_id: UUID, db: AsyncSession = Depends(get_session)):
    await service.delete_comment(db, comment_id)
    return {'detail': 'success'}
