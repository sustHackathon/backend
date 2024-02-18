from datetime import date

from typing import List
from pydantic import BaseModel, EmailStr
from typing import Union

from datetime import date, time


class Token(BaseModel):
    accessToken: str
    token_type: str
    email: EmailStr
    role: str
    name: str
    phone: str
    userName: str


class TokenData(BaseModel):
    email: EmailStr


class payload(BaseModel):
    email: EmailStr
    role: str
    phone: str
    name: str
    userName: str

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    phone: str
    name: str
    password: str
    role: str
    userName: str

    class Config:
        orm_mode = True
    

class AdminSignUp(BaseModel):
    email: EmailStr
    phone: str
    name: str
    password: str
    position: str

    class Config:
        orm_mode = True

class Admin(BaseModel):
    email: EmailStr
    phone: str
    name: str
    userName: str
    position: str

    class Config:
        orm_mode = True


class TouristSignUp(BaseModel):
    email: EmailStr
    phone: str
    name: str
    password: str

    class Config:
        orm_mode = True

class Tourist(BaseModel):
    email: EmailStr
    phone: str
    name: str
    userName: str

    class Config:
        orm_mode = True

class UserSignin(BaseModel):
    email: Union[EmailStr, str]
    password: str

    class Config:
        orm_mode = True

class bankAccount(BaseModel):

    userName: str
    accountHolderName: str
    balance: int
    class Config:
        orm_mode = True




class Room(BaseModel):
    roomType: str
    price: int
    available: int
    class Config:
        orm_mode = True


class Hotel(BaseModel):
    name: str
    location: str
    phone: str
    email: EmailStr
    password: str   
    description: str
    star: int
    rooms: List[Room]
    class Config:
        orm_mode = True


class HotelOut(BaseModel):
    name: str
    location: str
    phone: str
    email: EmailStr
    description: str
    star: int
    rooms: List[Room]
    class Config:
        orm_mode = True

class ToursitOut(BaseModel):
    email: EmailStr
    phone: str
    name: str
    userName: str
    balance: int
    class Config:
        orm_mode = True


class Booking(BaseModel):
    hotelUserName: str
    roomType: str
    checkIn: date
    totalRoom: int
    class Config:
        orm_mode = True


class ScheduleMail(BaseModel):
    place: str
    date : date
    time : str
    
    class Config:
        orm_mode = True