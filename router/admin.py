import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Admin"],
    prefix="/admin"
)


@router.get("/profile", response_model=schemas.Admin)
def getProfile(db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):
    if currentUser.role != "ADMIN" and db.query(models.Admin).filter(models.Founder.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    admin = db.query(models.Admin).filter(
        models.Admin.email == currentUser.email).first()
    return admin
