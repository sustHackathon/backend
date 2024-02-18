# main.py

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
import utils
from database import engine

from router import auth, chatBot, admin, forAll, tourist
import config
import schemas

from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chatBot.router)
app.include_router(admin.router)
app.include_router(forAll.router)
app.include_router(tourist.router)




