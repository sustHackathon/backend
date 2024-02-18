import ai
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import ai
from datetime import date

router = APIRouter(
    tags=["ChatBot"],
    prefix="/chatBot"
)


@router.get("", response_model=dict,
            status_code=200)
def getAnswer(question: str):
    response = ai.getAnswer(question)
    question += f"give me response without star(*).Give the ouput in readable format.\n{response}"
    return HTMLResponse(response)



@router.get("/getSpecificAnswer", response_model=dict,
            status_code=200)

def getSpecificAnswer( budget:int, currentCity: str, destination: str, startingDate: date, endingDate: date):
    question = f"I want to make a tour plan with {budget} taka. I am currently in {currentCity}. I want to go to {destination}. I want to start my tour on {startingDate} and end on {endingDate}. Give me output in the following format:(Don't Give any astericks(*) in the output.Present the output in a readable format)\n\
    Select transportation type: [bus, train, air]\n\
    If type=['bus'](giving a list of available buses in budget)\n\
        Then select bus type: [ac, non-ac]\n\
            Ticket price: [price] in taka\n\
            Bus company name: [companyName] like Hanif Enterprise/Shyamoli Paribahan, Green Line Enterprise, Royal Coach, etc.\n\
            Start time: [time] in 24-hour format\n\
            Starting place: [place]\n\
            End time: [time] in 24-hour format\n\
            Ending place: [place]\n\
    If type=['train'](giving a list of available trains in budget)\n\
        Then select train type: [ac, non-ac]\n\
            Ticket price: [price] in taka\n\
            Train name: [trainName] like Sundarban Express, Silk City Express, etc.\n\
            Start time: [time] in 24-hour format\n\
            Starting place: [place]\n\
            End time: [time] in 24-hour format\n\
            Ending place: [place]\n\
    If type=['air'](giving a list of available airs in budget)\n\
        Then select airline name: [airLineName] like Biman Bangladesh Airlines, Novoair, US-Bangla\n\
            Ticket type: [economy, business]\n\
            Ticket price: [price] in taka\n\
            Start time: [time] in 24-hour format\n\
            Starting place: [place]\n\
            End time: [time] in 24-hour format\n\
            Ending place: [place]\n\
    else not available in this budget\n\""
    
    
    response = ai.getAnswer(question)
    return HTMLResponse(response)
