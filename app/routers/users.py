from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import users

router= APIRouter(prefix="/user",tags=["Users"])
get_db= database.get_database

@router.post('', response_model=schemas.UsersOnly)
async def sign_up(request:schemas.UserSignup, db: Session=Depends(get_db)):
    return await users.sign_up(request, db)
