from fastapi import APIRouter, Depends, status
from ..import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import superuser
from typing import List

router= APIRouter(prefix='/superuser', tags=["Super User"])
get_db= database.get_database

@router.get('/{id}/view-user-by-id', response_model= List[schemas.AllUsersNews], status_code=status.HTTP_200_OK)
async def user_by_id(id, db: Session= Depends(get_db),current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await superuser.user_by_id(id, db, current_user)

@router.get('/view-all-news-users', response_model= List[schemas.AllNewsUsers], status_code=status.HTTP_200_OK)
async def all_news_users( db: Session= Depends(get_db),current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await superuser.all_news_users(db, current_user)

@router.get('/view-all-users-news', response_model= List[schemas.AllUsersNews], status_code=status.HTTP_200_OK)
async def all_users_news( db: Session= Depends(get_db),current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await superuser.all_users_news(db, current_user)