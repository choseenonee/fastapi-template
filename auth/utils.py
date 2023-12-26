from sqlalchemy.orm import Session

from auth.security import verify_password
from db.crud.user import get_user_by_login


def authenticate_user(db: Session, login: str, password: str):
    user = get_user_by_login(db, login)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
