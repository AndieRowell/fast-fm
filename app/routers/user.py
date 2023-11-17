from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import models
import schemas
import database

@app.route


@router.get("/all", response_model=List[schemas.Song]) 
def get_heroes(db: Session = Depends(get_db)):

    #create a get crud operation to return the list of heroes
    # db.query(models.User).offset(skip).limit(limit).all()
        #want to run a db query to get all the users
    heroes = crud.get_heroes(db)
    return heroes
