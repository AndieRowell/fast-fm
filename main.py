from fastapi import FastAPI, HTTPException, Depends, status
# not sure yet if this is where i want to place these imports...just yet but in case i forget for now
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
