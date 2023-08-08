from fastapi import status, Response, HTTPException
from .. import models
from typing import List


async def create_news(request, db, current_user):
    get_user_id= db.query(models.User).filter(models.User.username== current_user.username).first().id
    news= models.News(title= request.title, body= request.body, user_id= get_user_id)
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

async def view_news(db):
    return (db.query(models.News).all())

async def user_news(db, current_user):
    get_user= db.query(models.User).filter(models.User.username== current_user.username).first()
    if not get_user:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, 
                            detail= "Invalid User or unauthenticated User")
    get_news= db.query(models.News).filter(models.News.user_id== get_user.id)
    if not get_news:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "You have not posted any news")
    return get_news

async def delete_news(id, db, current_user):
    get_news= db.query(models.News).filter(models.News.id==id)
    if not get_news.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Either this news was already deleted or does not exist")
    get_news_backup= {"title":get_news.first().title, "body": get_news.first().body}
    get_news.delete(synchronize_session= False)
    db.commit()
    return Response(content= f"You deleted this data: {get_news_backup}")

async def update_news(id, request, db, current_user):
    get_id= db.query(models.News).filter(models.News.id==id)
    if not get_id.first() or get_id.first().creator.username!= current_user.username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="there is no news with this id, news does not exist")
    get_id.update(request.model_dump())
    db.commit()
    updated_news= {'title': get_id.first().title, 'body': get_id.first().body}
    return Response(content=f"Updated successfully: {updated_news} ")
    