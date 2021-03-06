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
    # home = crud.get_complaints(db, skip=skip, limit=limit)
    return templates.TemplateResponse("index.html", {"request": request})


## start API and template routes


@app.get("/random_api")
def read_random(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    random = crud.get_random(db, skip=skip, limit=limit)
    return random


@app.get("/random")
def show_random(request: Request):
    return templates.TemplateResponse("random.html", {"request": request})


@app.get("/zipcode_api")
def read_zip_stats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zip_stats = crud.get_zip_stats(db, skip=skip, limit=limit)
    return zip_stats


@app.get("/zipcode")
def show_zip_stats(request: Request):
    return templates.TemplateResponse("zipcode.html", {"request": request})


@app.get("/distance_api")
def read_distance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    distance = crud.get_distance(db, skip=skip, limit=limit)
    return distance


@app.get("/distance")
def show_distance(request: Request):
    return templates.TemplateResponse("long.html", {"request": request})


@app.get("/duration_api")
def read_duration(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    duration = crud.get_duration(db, skip=skip, limit=limit)
    return duration


@app.get("/duration")
def show_duration(request: Request):
    return templates.TemplateResponse("long.html", {"request": request})


@app.get("/redzone_api")
def read_red_zone(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    red_zone = crud.get_red_zone(db, skip=skip, limit=limit)
    return red_zone


@app.get("/redzone")
def show_red_zone(request: Request):
    return templates.TemplateResponse("redzone.html", {"request": request})


@app.get("/zero_distance_api")
def read_zero_distance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zero_distance = crud.get_zero_distance(db, skip=skip, limit=limit)
    return zero_distance


@app.get("/zero_distance")
def show_zero_distance(request: Request):
    return templates.TemplateResponse("nowhere.html", {"request": request})


## start API only routes


@app.get("/complaints_api")
def read_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    complaints = crud.get_complaints(db, skip=skip, limit=limit)
    return complaints


@app.get("/scooter_trips")
def read_trips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trips = crud.get_trips(db, skip=skip, limit=limit)
    return trips


@app.get("/zero_zip_code_api")
def read_zero_zip_code(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zero_zip_code = crud.get_zero_zip_code(db, skip=skip, limit=limit)
    return zero_zip_code


@app.get("/zero_month_api")
def read_zero_month(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zero_month = crud.get_zero_month(db, skip=skip, limit=limit)
    return zero_month


@app.get("/zero_weekday_api")
def read_zero_weekday(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zero_weekday = crud.get_zero_weekday(db, skip=skip, limit=limit)
    return zero_weekday


@app.get("/zero_hour_api")
def read_zero_hour(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    zero_hour = crud.get_zero_hour(db, skip=skip, limit=limit)
    return zero_hour


# if __name__ == "__main__":
#     app.run(debug=True)
