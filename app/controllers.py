from typing import List

from fastapi import FastAPI, Response, Request, Cookie, Depends
from pydantic.main import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app import service
from app.base import get_session
from models import User


app = FastAPI()


class UserSchema(BaseModel):
    username: str
    password: int
    email: str


@app.get("/", response_model=List[UserSchema])
async def get_users(request: Request, response: Response, session: AsyncSession = Depends(get_session)):
    request = request
    response = response
    users = await service.get_users(session)
    # return {"message": "Hello World"}
    return [UserSchema(username=c.username, password=c.password, email=c.email) for c in users]


@app.post("/post/")
async def add_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    user = service.add_user(session, user.username, str(user.password), user.email)
    try:
        await session.commit()
        return user
    except IntegrityError as ex:
        await session.rollback()
        # raise DuplicatedEntryError("The city is already stored")
        raise Exception