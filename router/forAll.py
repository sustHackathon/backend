import models
import schemas
import utils
import oauth2
import database
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["For All"]
)


@router.get("/getAllHotels",
            status_code=200)
def getAllHotels(db: Session = Depends(database.get_db)):
    hotel = db.query(models.Hotel).join(
        models.Room, models.Hotel.userName == models.Room.hotelUserName).all(
    )

    hotelWithRoom = {}
    for hotel in hotel:
        hotelWithRoom[hotel.userName] = hotel

        rooms = db.query(models.Room).filter(
            models.Room.hotelUserName == hotel.userName).all()
        roomList = []
        for room in rooms:
            roomList.append(room)
        hotelWithRoom[hotel.userName].rooms = roomList

    return hotelWithRoom


@router.get("/getHotel",
            status_code=200)
def getHotel(search: str, db: Session = Depends(database.get_db)):
    hotel = db.query(models.Hotel).join(
        models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Hotel.name.like(f"%{search}%")).all()
    hotel += db.query(models.Hotel).join(
        models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Room.roomType.like(f"%{search}%")).all()
    hotel += db.query(models.Hotel).join(
        models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Hotel.location.like(f"%{search}%")).all()

    if str(search).isdigit():
        hotel += db.query(models.Hotel).join(
            models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Room.price <= int(search)).all()
        hotel += db.query(models.Hotel).join(
            models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Room.available >= int(search)).all()
        hotel += db.query(models.Hotel).join(
            models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Room.id == int(search)).all()
        hotel += db.query(models.Hotel).join(
            models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Hotel.star == int(search)).all()
        hotel += db.query(models.Hotel).join(
            models.Room, models.Hotel.userName == models.Room.hotelUserName).filter(models.Hotel.rating == int(search)).all()

    hotelWithRoom = {}
    for hotel in hotel:
        hotelWithRoom[hotel.userName] = hotel

        rooms = db.query(models.Room).filter(
            models.Room.hotelUserName == hotel.userName).all()
        roomList = []
        for room in rooms:
            roomList.append(room)
        hotelWithRoom[hotel.userName].rooms = roomList

    return hotelWithRoom
