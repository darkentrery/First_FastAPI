from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.models import *


async def get_users(session: AsyncSession) -> List[User]:
    result = await session.execute(select(User).order_by(User.id.desc()).limit(20))
    return result.scalars().all()


def add_user(session: AsyncSession, username: str, password: str, email: str):
    user = User(username=username, password=password, email=email)
    session.add(user)
    return user