from sqlalchemy.orm import Session

# from fastapi.encoders import jsonable_encoder
from . import models, schemas
import json


def get_trips(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trip).offset(skip).limit(limit).all()


def get_random(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT s.* FROM scooter_data AS s \
        INNER JOIN (SELECT ROUND(RAND() * (SELECT MAX(trip_id) FROM scooter_data )) AS rand_id) AS x \
        WHERE s.trip_id = x.rand_id LIMIT 1;"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT t.latitude_coord AS 'SR_Location_Lat' ,t.longitude_coord AS 'SR_Location_Lon' \
        ,t.zip_code AS 'SR_Location_Zip_Code' FROM 311_data t \
        WHERE t.sr_desc = 'Shared Micromobility' AND t.zip_code > 0"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_distance(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM distance_10_chart")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_duration(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM duration_10_chart")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_distance(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute("SELECT * FROM zero_distance_chart")
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)
