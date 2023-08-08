from fastapi import APIRouter, Depends, status
from ..import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import news
from typing import List

router= APIRouter(prefix="/news", tags=['News'])
get_db= database.get_database

@router.post('', response_model= schemas.NewsModel, status_code=status.HTTP_201_CREATED)
async def create_news(request: schemas.NewsModel, db:Session= Depends(get_db), current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await news.create_news(request, db, current_user)

@router.get('', response_model= List[schemas.NewsModel], status_code= status.HTTP_200_OK)
async def view_news(db: Session= Depends(get_db), current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await news.view_news(db)

@router.get('/my-news', response_model= List[schemas.NewsModel], status_code=status.HTTP_200_OK)
async def user_news( db: Session= Depends(get_db),current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await news.user_news(db, current_user)

@router.get('/{id}/delete-news', status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(id, db:Session= Depends(get_db), current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await news.delete_news(id, db, current_user)

@router.put('/{id}/update-news', status_code=status.HTTP_202_ACCEPTED)
async def update_news(id,request: schemas.NewsModel, db:Session= Depends(get_db), current_user: schemas.UserLogin= Depends(oauth2.get_current_user)):
    return await news.update_news(id, request, db, current_user)



