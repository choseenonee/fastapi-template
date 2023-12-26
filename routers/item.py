from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from db.db import SessionLocal
from dependencies import is_admin, get_db
from db.models.item import Item, ItemCreate
from db.crud.item import create_item, get_item_by_id


router = APIRouter(
    prefix="/item",
    tags=["items"],
    responses={404: {"description": "Not found"},
               500: {"description": "Internal server error"},
               403: {"description": "only admin user can create items"}},
)


@router.post("/create", response_model=Item)
async def create(item: ItemCreate, access: Annotated[bool, Depends(is_admin)], db: SessionLocal = Depends(get_db)):
    if access:
        try:
            db_item = create_item(db, item)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")
        return db_item
    else:
        raise HTTPException(status_code=403, detail="only admin user can create items")


@router.get("/get_by_id/{item_id}", response_model=Item)
async def get_user(item_id: int, db: SessionLocal = Depends(get_db)):
    item = get_item_by_id(db, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Not found")

    return item