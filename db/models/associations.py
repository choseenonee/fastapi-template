from sqlalchemy import Table, Column, ForeignKey

from .base import Base


user_item = Table(
    "user_item",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("item_id", ForeignKey("item.id"), unique=True),
)