from sqlalchemy.orm import Session

# from fastapi.encoders import jsonable_encoder
from . import models, schemas
import json


def get_trips(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trip).offset(skip).limit(limit).all()

# def get_random(db: Session, skip: int = 0, limit: int = 100):
#    res = db.execute(
#
#    )
#    res_str = json.dumps([dict(r) for r in res])
#    return json.loads(res_str)


def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM complaints_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_distance(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM distance_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_duration(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM duration_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_distance(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT * FROM zero_distance_plot z ORDER BY z.trip_duration desc;"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_zip_code(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM zero_zip_code_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_month(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM zero_month_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_weekday(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM zero_weekday_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_hour(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM zero_hour_plot;")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)
