from sqlalchemy import delete, update, select
from sqlalchemy.orm import Session

from auth.security import get_password_hash
from ..models.user import *


def create_user(db: Session, user: UserCreate) -> SqlUser:
    db_user = SqlUser(**user.model_dump(exclude="password"), hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: User):
    update_query = update(SqlItem).where(SqlItem.id == user.id).values(user)
    db.execute(update_query)
    db.commit()


def get_user_by_id(db: Session, user_id: int) -> SqlUser:
    return db.query(SqlUser).filter(SqlUser.id == user_id).one_or_none()


def get_user_by_login(db: Session, login: str) -> SqlUser:
    return db.query(SqlUser).filter(SqlUser.login == login).one_or_none()


def delete_user_by_id(db: Session, user_id: int):
    db.execute(delete(SqlUser).where(SqlUser.id == user_id))
