from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel

from .base import Base


class ItemCreate(BaseModel):
    name: str
    is_taken: bool


class Item(ItemCreate):
    id: int

    class Config:
        from_attributes = True


class SqlItem(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    is_taken: Mapped[bool] = mapped_column(Boolean)
