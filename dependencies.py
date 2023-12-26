from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from auth.jwt import decode_access_token, credentials_exception
from db.crud.user import get_user_by_id
from db.db import SessionLocal
from db.models.user import SqlUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: SessionLocal = Depends(get_db)):
    token_data = decode_access_token(token)
    user = get_user_by_id(db, token_data.id)
    if user is None:
        raise credentials_exception
    return user


async def is_admin(user: Annotated[SqlUser, Depends(get_current_user)]):
    return user.is_admin
