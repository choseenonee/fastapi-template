from typing import List

from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel

from .base import Base
from .associations import user_item
from .item import SqlItem, Item


class UserBase(BaseModel):
    login: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_admin: bool
    items: List[Item]

    class Config:
        from_attributes = True


# an example mapping using the base
class SqlUser(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    items: Mapped[List[SqlItem]] = relationship(secondary=user_item)
