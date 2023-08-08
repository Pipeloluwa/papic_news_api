from .. import models
from ..hashing import Hash

async def sign_up(request, db):
    new_user= models.User(username=request.username,
                          email= request.email,
                          password= Hash.enc(request.password)
                          )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

