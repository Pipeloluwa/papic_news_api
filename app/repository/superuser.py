from fastapi import status, Response, HTTPException
from .. import models
from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

async def user_by_id(id, db, current_user):
    check_super_id= db.query(models.User).filter(models.User.username== current_user.username).first().id
    if not current_user.username == os.getenv("POSTGRES_USER") and check_super_id == os.getenv("SUPERUSER_ID"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Either you are not authorized or you are not permitted to view this content")
    get_user= db.query(models.User).filter(models.User.id==id)
    if not get_user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "There is no news nor users")
    return get_user
    

async def all_news_users(db, current_user):
    check_super_id= db.query(models.User).filter(models.User.username== current_user.username).first().id
    if not current_user.username == os.getenv("POSTGRES_USER") and check_super_id == os.getenv("SUPERUSER_ID"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Either you are not authorized or you are not permitted to view this content")
    get_news= db.query(models.News).all()
    if not get_news:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "There is no news nor users")
    return get_news

async def all_users_news(db, current_user):
    check_super_id= db.query(models.User).filter(models.User.username== current_user.username).first().id
    if not current_user.username == os.getenv("POSTGRES_USER") and check_super_id == os.getenv("SUPERUSER_ID"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Either you are not authorized or you are not permitted to view this content")
    get_users= db.query(models.User).all()
    if not get_users:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "There is no news nor users")
    return get_users