from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

import datetime as dt
import numpy as np
import random

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def home(request: Request):
    # list of links to other routes
    return templates.TemplateResponse("index.html", {"request": request})


# API Routes
@app.get("/complaints", response_model=List[schemas.Complaint])
def read_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    complaints = crud.get_complaints(db, skip=skip, limit=limit)
    return complaints


@app.get("/queries")
def read_queries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    queries = crud.get_queries(db, skip=skip, limit=limit)
    return queries


@app.get("/scooter_trips", response_model=List[schemas.Trip])
def read_trips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trips = crud.get_trips(db, skip=skip, limit=limit)
    return trips


@app.get("/random")
def generate_scooter(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    random = crud.get_random(db, skip=skip, limit=limit)
    return random


@app.get("/{zipcode}")
def zip_stats(zipcode, request: Request):
    # % compaint, # rides in,m # rides out, max expense, min expense, avg, complaints, maps and other stats
    return templates.TemplateResponse(
        "index.html", {"request": request, "zipcode": zipcode}
    )


@app.get("/long")
def longest(request: Request):
    # display longest ride distance/time
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/nowhere")
def nowhere(request: Request):
    # rides that go nowhere, some plots on this. where/when
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/red_zone")
def red_zone(request: Request):
    #  red zone zip code (10 worst neighbor hoods to leave scooter in)
    return templates.TemplateResponse("index.html", {"request": request})


# if __name__ == "__main__":
#     app.run(debug=True)
