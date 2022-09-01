
from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)


class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=True)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
