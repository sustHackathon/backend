import httpx
import logging
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi import FastAPI
import random
from fastapi import Depends
from datetime import date, timedelta, datetime
from enum import Enum
import models
import database
from passlib.context import CryptContext
from datetime import datetime, timedelta
from email.message import EmailMessage
import ssl
import smtplib
import config
import schedule
import time
import models
import schemas
import oauth2
import database
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from models import ScheduleMail  # Assuming you have a model named ScheduleMail


from sqlalchemy import create_engine, select


from email.header import Header

from email.utils import formataddr

from fastapi import Depends, HTTPException, APIRouter


pwdContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


logging.basicConfig(level=logging.INFO)


emailSender = config.Settings.email_sender
emailPassword = config.Settings.email_password


def hash(password: str):
    return pwdContext.hash(password)


def verify(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)



def createUserName(name: str):
    name = name.lower()
    name = name.split(" ")
    if len(name) == 1:
        userName = name[0]+str(random.randint(0, 9999))

    else:
        userName = name[0]+name[1]+str(random.randint(0, 9999))
    return userName

# send message to user


def sendEmail(subject: str, body: str, receiver_email: str):
    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = formataddr((str(Header('Trip Mate', 'utf-8')), emailSender))
    message["To"] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(emailSender, emailPassword)
        server.send_message(message)

