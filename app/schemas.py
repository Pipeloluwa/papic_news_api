from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic.types import SecretStr, constr

#FILL FORMS
class UserLogin(BaseModel):
    username: str
    password: str

class UserSignup(UserLogin):
    email: str
    class Config():
        from_attributes= True

class NewsModel(BaseModel):
    title: str
    body: str
    class Config():
        from_attributes= True




#FORMS FOR DISPLAYING RESULTS
class UsersOnly(BaseModel):
    username: str
    email: str
    class Config():
        from_attributes= True

class AllNewsUsers(NewsModel):
    creator: UsersOnly
    class Config():
        from_attributes= True

class AllUsersNews(UsersOnly):
    news_data: List[NewsModel]=[]
    class Config():
        from_attributes= True



#LOGIN TOKEN
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenDataUser(BaseModel):
    username: Optional[str]= None

class FilesData(BaseModel):
    pass


#MEDIA SECTION
class Item(BaseModel):
    id: str
    value: str


class Media(BaseModel):
    username: constr(to_lower=True)
    is_uploaded: bool= Field(default=False)
    image: Optional[str]= None

class Media2(BaseModel):
    filename: constr(to_lower=True)

