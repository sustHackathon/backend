import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/signup", response_model=schemas.Tourist, status_code=201)
def signup(tourist: schemas.TouristSignUp, db: Session = Depends(database.get_db)):
    if db.query(models.User).filter(models.User.email == tourist.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    userName = utils.createUserName(tourist.name)
    while True:
        if not db.query(models.User).filter(models.User.userName == userName).first():
            break
        userName = utils.createUserName(tourist.name)

    tourist.phone = str("+88")+tourist.phone
    user = models.User(email=tourist.email, phone=tourist.phone, name=tourist.name,
                       password=utils.hash(tourist.password), role="TOURIST", userName=userName)

    db.add(user)
    db.commit()
    db.refresh(user)

    tourist = models.Tourist(
        email=tourist.email, phone=tourist.phone, name=tourist.name, userName=userName)

    db.add(tourist)
    db.commit()
    db.refresh(tourist)

    bankAccount = models.bankAccount(
        userName=userName, accountHolderEmail=tourist.email, accountHolderName=tourist.name, balance=10000)

    db.add(bankAccount)
    db.commit()
    db.refresh(bankAccount)

    utils.sendEmail(
        "Welcome to TripMate ",
        f"Hello {tourist.name}, Welcome to our platform. Your username is {userName}. You can use this username to login to our platform. You have a gift bonus of 10000 BDT. Thank you.", tourist.email
    )

    return tourist


@router.post("/signin", response_model=schemas.Token)
def signin(
    credential: schemas.UserSignin,
    db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(
        (models.User.email == credential.email) |
        (models.User.userName == credential.email)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="emailError")
    if not utils.verify(credential.password, user.password):
        raise HTTPException(status_code=404, detail="passwordError")

    access_token = oauth2.createAccessToken(
        data={"email": user.email, "role": user.role, "name": user.name, "phone": user.phone, "userName": user.userName})

    tokenData = schemas.Token(name=user.name, email=user.email, role=user.role,
                              accessToken=access_token, phone=user.phone, token_type="Bearer", userName=user.userName)
    return tokenData


@router.post("/signup/admin", response_model=schemas.Admin, status_code=201)
def signup_founder(admin: schemas.AdminSignUp, db: Session = Depends(database.get_db)):
    if db.query(models.User).filter(models.User.email == admin.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    userName = utils.createUserName(admin.name)
    while True:
        if not db.query(models.User).filter(models.User.userName == userName).first():
            break
        userName = utils.createUserName(admin.name)

    admin.phone = str("+88")+admin.phone
    user = models.User(email=admin.email, phone=admin.phone, name=admin.name,
                       password=utils.hash(admin.password), role="ADMIN", userName=userName)

    db.add(user)
    db.commit()
    db.refresh(user)

    admin = models.Admin(
        email=admin.email, phone=admin.phone, name=admin.name, userName=userName, position=admin.position)

    db.add(admin)
    db.commit()
    db.refresh(admin)

    utils.sendEmail("Welcome to TripMate",
                    f"Hello {admin.name}, Welcome to our platform. Your username is {userName}. You can use this username to login to our platform. Thank you.", admin.email)

    return admin


@router.post("/signup/hotel", response_model=dict, status_code=201)
def signupHotel(htl: schemas.Hotel, db: Session = Depends(database.get_db)):
    if db.query(models.User).filter(models.User.email == htl.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    userName = utils.createUserName(htl.name)
    while True:
        if not db.query(models.User).filter(models.User.userName == userName).first():
            break
        userName = utils.createUserName(htl.name)

    htl.phone = str("+88")+htl.phone
    user = models.User(email=htl.email, phone=htl.phone, name=htl.name,
                       password=utils.hash(htl.password), role="HOTEL", userName=userName)

    db.add(user)
    db.commit()
    db.refresh(user)

    hotel = models.Hotel(
        userName=userName, name=htl.name, location=htl.location, phone=htl.phone, email=htl.email, description=htl.description, rating=0, star=htl.star)

    db.add(hotel)
    db.commit()
    db.refresh(hotel)

    for room in htl.rooms:
        room = models.Room(
            hotelUserName=userName, roomType=room.roomType, price=room.price, available=room.available)

        db.add(room)
        db.commit()
        db.refresh(room)

    utils.sendEmail("Welcome to TripMate",
                    f"Hello {htl.name}, Welcome to our platform. Your username is {userName}. You can use this username to login to our platform. Thank you.", htl.email)

    return {"message": "SUCCESSFULL"}
