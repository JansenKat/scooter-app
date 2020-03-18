from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

import datetime as dt
import numpy as np
import random

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=
#     allow_headers=
#     allow_credentials=True
# )

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    # list of links to other routes
    return templates.TemplateResponse("index.html")

# @app.get("/random")
# def generate_scooter():
#     # generate random # - display scooter ride
#     return render_template("index.html")

# @app.get("/difference")
# def zipcode_vs_census():
#     # 2 addresses same zipcode, diff census track, how the data differs
#     return render_template("index.html")

# @app.get("/{zipcode}")
# def zip_stats():
#     # % compaint, # rides in,m # rides out, max expense, min expense, avg, complaints, maps and other stats
#     return render_template("index.html")

# @app.get("/long")
# def longest():
#     # display longest ride distance/time
#     return render_template("index.html")

# @app.get("/nowhere")
# def nowhere():
#     # rides that go nowhere, some plots on this. where/when
#     return render_template("index.html")

# @app.get("/red_zone")
# def red_zone():
#     #  red zone zip code (10 worst neighbor hoods to leave scooter in)
#     return render_template("index.html")


#API Routes
@app.get("/complaints/", response_model=List[schemas.Complaint])
def read_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_complaints(db, skip=skip, limit=limit)
    return users

@app.get("/scooter_trips/", response_model=List[schemas.Trip])
def read_trips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_trips(db, skip=skip, limit=limit)
    return items

# @app.get("/api_docs")
# def api_docs():
#     # Documentation for API
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)