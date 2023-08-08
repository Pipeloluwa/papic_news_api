from fastapi import APIRouter, Depends, HTTPException, status
from ..import database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm= Depends(), db: Session= Depends(database.get_database)):
    user= db.query(models.User).filter(models.User.username== request.username).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail= "Check what you typed,because This username does not exist")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= "your password is incorrect")
    access_token= token.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}