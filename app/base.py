from os import environ

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


POSTGRES_USER = environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_NAME = environ.get("POSTGRES_NAME", "postgres")
POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5437/{POSTGRES_NAME}"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
