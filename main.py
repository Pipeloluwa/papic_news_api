from fastapi import FastAPI, status, Response
from app.database import engine
from app import  models
from app.routers import users, news, authentication, superuser, file_uploads
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(news.router)
app.include_router(authentication.router)
app.include_router(superuser.router)
app.include_router(file_uploads.router)

@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return Response(content= "This is PAPIC API, ask the developer for the routers available!")
