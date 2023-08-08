from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__= 'users'
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    email= Column(String)
    password= Column(String)

    news_data= relationship('News', back_populates='creator')

class News(Base):
    __tablename__= 'news'
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String)
    body= Column(String)
    
    user_id= Column(Integer, ForeignKey('users.id'))
    creator= relationship('User', back_populates='news_data')

# class Media(Base):
#     title= Column(String)

