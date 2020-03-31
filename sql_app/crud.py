from sqlalchemy.orm import Session

# from fastapi.encoders import jsonable_encoder
from . import models, schemas
import json


def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Complaint).offset(skip).limit(limit).all()


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


def get_queries(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT s.trip_duration ,s.trip_distance ,s.census_tract_start ,s.census_tract_end, s.census_tract_end, \
        1 + 0.15 * (s.trip_duration/60) as 'cost' \
        FROM scooter_data s \
        ORDER BY trip_duration desc LIMIT 10;"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


# vehicle_id = Column(String)
# vehicle_type = Column(String)
# trip_duration = Column(Float)
# trip_distance = Column(Float)
# start_time = Column(String)
# end_time = Column(String)
# modified_date = Column(String)
# council_dist_start = Column(String)
# council_dist_end = Column(String)
# year = Column(Integer)
# census_tract_start = Column(String)
# census_tract_end = Column(String)
