from os import environ

import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey


POSTGRES_USER = environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_NAME = environ.get("POSTGRES_NAME", "postgres")
POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)


# metadata = sqlalchemy.MetaData()
#
#
# users_table = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
#     sqlalchemy.Column("name", sqlalchemy.String(100)),
#     sqlalchemy.Column("hashed_password", sqlalchemy.String()),
#     sqlalchemy.Column(
#         "is_active",
#         sqlalchemy.Boolean(),
#         server_default=sqlalchemy.sql.expression.true(),
#         nullable=False,
#     ),
# )
#
#
# tokens_table = sqlalchemy.Table(
#     "tokens",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column(
#         "token",
#         UUID(as_uuid=False),
#         server_default="1234",
#         unique=True,
#         nullable=False,
#         index=True,
#     ),
#     sqlalchemy.Column("expires", sqlalchemy.DateTime()),
#     sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
# )
#
#
# posts_table = sqlalchemy.Table(
#     "posts",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
#     sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
#     sqlalchemy.Column("title", sqlalchemy.String(100)),
#     sqlalchemy.Column("content", sqlalchemy.Text()),
# )