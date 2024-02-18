
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta
from sqlalchemy import DateTime

from sqlalchemy import Date

from sqlalchemy import Time


class User(Base):
    __tablename__ = "users"
    email = Column(String, unique=True, index=True, primary_key=True)
    phone = Column(String)
    name = Column(String)
    password = Column(String)
    role = Column(String)
    userName = Column(String, unique=True, index=True)


class Admin(Base):
    __tablename__ = "admins"
    email = Column(String, ForeignKey("users.email"), primary_key=True)
    phone = Column(String)
    name = Column(String)
    userName = Column(String, ForeignKey("users.userName"))
    position = Column(String)


class Tourist(Base):
    __tablename__ = "tourists"
    email = Column(String, ForeignKey("users.email"), primary_key=True)
    phone = Column(String)
    name = Column(String)
    userName = Column(String, ForeignKey("users.userName"))


class bankAccount(Base):
    __tablename__ = "bankAccounts"
    userName = Column(String, ForeignKey("users.userName"), primary_key=True)
    accountHolderEmail = Column(String, ForeignKey("users.email"))
    accountHolderName = Column(String)
    balance = Column(Integer)


class Hotel(Base):
    __tablename__ = "hotels"
    userName = Column(String, ForeignKey("users.userName"), primary_key=True)
    name = Column(String)
    location = Column(String)
    phone = Column(String)
    email = Column(String)
    description = Column(String)
    rating = Column(Integer)
    star = Column(Integer)


class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hotelUserName = Column(String, ForeignKey("users.userName"))
    roomType = Column(String)
    price = Column(Integer)
    available = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    touristUserName = Column(String, ForeignKey("users.userName"))
    checkIn = Column(DateTime)
    hotelUserName = Column(String, ForeignKey("users.userName"))
    roomType = Column(String)
    totalRoom = Column(Integer)
    totalCost = Column(Integer)


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bookingId = Column(Integer, ForeignKey("bookings.id"))
    amount = Column(Integer)
    date = Column(DateTime)
    status = Column(String)


class ScheduleMail(Base):
    __tablename__ = "schedulemails"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    place = Column(String)
    date = Column(Date)
    time = Column(String)
    email = Column(String, ForeignKey("users.email"))