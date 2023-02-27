from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .exceptions import ItemNotFound, ItemAlreadyExists
from .users.router import users
from .actions.comments.router import comments as comment_router
from .actions.news.router import news as news_router


app = FastAPI(
    title='Car Web Service'
)


@app.exception_handler(ItemNotFound)
async def on_not_found(request: Request, exc: ItemNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'detail': 'item not found' if len(exc.args) == 0 else exc.args[0]}
    )


@app.exception_handler(ItemAlreadyExists)
async def on_already_exists(request: Request, exc: ItemAlreadyExists):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': 'item already exists' if len(exc.args) == 0 else exc.args[0]}
    )


app.include_router(users)
app.include_router(comment_router)
app.include_router(news_router)
