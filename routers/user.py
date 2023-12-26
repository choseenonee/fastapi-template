from fastapi import APIRouter, Depends, HTTPException

from db.db import SessionLocal
from dependencies import get_db
from db.models.user import UserCreate, User
from db.crud.user import create_user, get_user_by_id


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}, 500: {"description": "Internal server error"}},
)


@router.post("/create", response_model=User)
async def create(user: UserCreate, db: SessionLocal = Depends(get_db)):
    try:
        db_user = create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return db_user


@router.get("/get_by_id/{user_id}", response_model=User)
async def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="Not found")

    return user
