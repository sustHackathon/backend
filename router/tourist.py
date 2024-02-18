import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from datetime import date
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import ai


router = APIRouter(
    tags=["Tourist"],
    prefix="/tourist"
)


@router.get("/profile", response_model=schemas.ToursitOut,
            status_code=200)
def getProfile(db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):
    if currentUser.role != "TOURIST" and db.query(models.Tourist).filter(models.Tourist.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    tourist = db.query(models.Tourist).filter(
        models.Tourist.email == currentUser.email).first()

    balance = db.query(models.bankAccount).filter(
        models.bankAccount.userName == tourist.userName).first()
    tourist = schemas.ToursitOut(
        email=tourist.email, phone=tourist.phone, name=tourist.name, userName=tourist.userName, balance=balance.balance)
    return tourist


@router.put("/recharge", response_model=dict,
            status_code=200)
def rechargeAccount(amount: int, db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):
    if currentUser.role != "TOURIST" and db.query(models.Tourist).filter(models.Tourist.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    tourist = db.query(models.Tourist).filter(
        models.Tourist.email == currentUser.email).first()
    balance = db.query(models.bankAccount).filter(
        models.bankAccount.userName == tourist.userName).first()
    balance.balance += amount
    db.commit()
    db.refresh(balance)
    tourist = schemas.Tourist(
        email=tourist.email, phone=tourist.phone, name=tourist.name, userName=tourist.userName, balance=balance.balance)

    utils.sendEmail("Recharge Successful",
                    f"Hello {tourist.name}, Your account has been recharged with {amount} taka. Your current balance is {balance.balance} taka. Thank you.", tourist.email)

    return {"message": "RECHARGED"}


@router.post("/booking",
             status_code=200)
def getBooking(booking: schemas.Booking, db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):
    if currentUser.role != "TOURIST" and db.query(models.Tourist).filter(models.Tourist.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    tourist = db.query(models.Tourist).filter(
        models.Tourist.email == currentUser.email).first()
    balance = db.query(models.bankAccount).filter(
        models.bankAccount.userName == tourist.userName).first()

    hotel = db.query(models.Hotel).join(
        models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Room.roomType == booking.roomType).first()

    hotelWithRoom = {}
    hotelWithRoom[hotel.userName] = hotel
    rooms = db.query(models.Room).filter(
        models.Room.hotelUserName == hotel.userName).all()
    roomList = []
    for room in rooms:
        if room.roomType == booking.roomType and room.available >= booking.totalRoom:
            roomList.append(room)
    hotelWithRoom[hotel.userName].rooms = roomList

    if hotelWithRoom[hotel.userName].rooms:
        if balance.balance >= booking.totalRoom*hotelWithRoom[hotel.userName].rooms[0].price:
            balance.balance -= booking.totalRoom * \
                hotelWithRoom[hotel.userName].rooms[0].price

            hotelWithRoom[hotel.userName].rooms[0].available -= booking.totalRoom
            db.commit()
            db.refresh(balance)
            tourist = schemas.Tourist(
                email=tourist.email, phone=tourist.phone, name=tourist.name, userName=tourist.userName, balance=balance.balance)
            utils.sendEmail("Booking Successful",
                            f"Hello {tourist.name}, Your booking has been confirmed. Your current balance is {balance.balance} taka. Thank you.", tourist.email)

            booking = models.Booking(
                touristUserName=tourist.userName, checkIn=booking.checkIn, hotelUserName=hotel.userName, roomType=booking.roomType, totalRoom=booking.totalRoom, totalCost=booking.totalRoom*hotelWithRoom[hotel.userName].rooms[0].price)
            db.add(booking)
            db.commit()
            db.refresh(booking)

            payment = models.Payment(
                bookingId=booking.id, amount=booking.totalCost, date=date.today(), status="PAID")
            db.add(payment)
            db.commit()
            db.refresh(payment)

            return {
                "hotel": hotelWithRoom[hotel.userName],
                "tourist": tourist,
                "booking": booking,
                "payment": payment
            }
        else:
            raise HTTPException(status_code=400, detail="balanceError")

    else:
        raise HTTPException(status_code=400, detail="availabilityError")


@router.get("/askAiForBudgetTour", response_model=dict,
            status_code=200)
def getBooking(city: str, db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):
    if currentUser.role != "TOURIST" and db.query(models.Tourist).filter(models.Tourist.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")
    balance = db.query(models.bankAccount).filter(
        models.bankAccount.userName == currentUser.userName).first()

    question = f"i want to go to {city} for a budget tour. I have {balance.balance} taka. Can you Suggest me? Don't give any star(*) in response"
    response = ai.getAnswer(question)
    response = f"******You have {balance.balance}taka******* \n {response}"

    return HTMLResponse(response)


@router.get("/budgetFriendlyAccomodation", response_model=dict,
            status_code=200)
def getBooking(city: str, budget: int,  currentUser=Depends(oauth2.getCurrentUser)):
    question = f"I want to go to {city} for a budget tour. I have {budget} taka. Can you suggest me some hotels in my range? Don't give any star(*) in response\n\
    HotelName: [hotelName]\n\
    Location: [location]\n\
    AvailableRoom: [availableRoom]\n\
    If availableRoom > 0\n\
        Then RoomType: [roomType]\n\
            Price: [price] in taka\n\
            Star: [star]\n\
            Rating: [rating]\n\
            Amenities: [amenities]\n\
            CustomerReview: [customerReview]"

    response = ai.getAnswer(question)
    return HTMLResponse(response)


@router.post("/setSchedule", response_model=dict,
             status_code=200)


def setSchedule(schedule: schemas.ScheduleMail, db: Session = Depends(database.get_db), currentUser=Depends(oauth2.getCurrentUser)):

    if currentUser.role != "TOURIST" and db.query(models.Tourist).filter(models.Tourist.email != currentUser.email).first():
        raise HTTPException(status_code=400, detail="emailError")

    schedule = models.ScheduleMail(
         date=schedule.date, time=schedule.time, place=schedule.place,
         email=currentUser.email)
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return {"message": "SCHEDULED"}