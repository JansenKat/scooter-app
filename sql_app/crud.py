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


def get_zero_zip_code(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT t.zip_code ,sum(c.ride_count) FROM census_tract_count c \
	    JOIN tract_to_zip t ON t.census_tract = c.census_tract_start \
	    GROUP BY t.zip_code ORDER BY sum(c.ride_count) desc LIMIT 20;"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_month(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT monthname(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) as 'month_name' \
        ,count(trip_duration) FROM zero_distance_chart z \
        GROUP BY monthname(str_to_date(z.start_time, '%c/%e/%Y %H:%i'));"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_weekday(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT CASE \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 1 THEN 'Sunday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 2 THEN 'Monday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 3 THEN 'Tuesday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 4 THEN 'Wednesday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 5 THEN 'Thursday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 6 THEN 'Friday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 7 THEN 'Saturday' \
		END AS 'weekday' \
	    ,count(trip_duration) \
        FROM zero_distance_chart z GROUP BY CASE \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 1 THEN 'Sunday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 2 THEN 'Monday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 3 THEN 'Tuesday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 4 THEN 'Wednesday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 5 THEN 'Thursday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 6 THEN 'Friday' \
		WHEN dayofweek(str_to_date(z.start_time, '%c/%e/%Y %H:%i')) = 7 THEN 'Saturday' \
		END;"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)


def get_zero_hour(db: Session, skip: int = 0, limit: int = 100):
    res = db.execute(
        "SELECT CAST(hour(str_to_date(start_time, '%c/%e/%Y %h:%i:%s %p')) AS CHAR(2)) AS 'hour' \
        ,count(trip_duration) FROM zero_distance_chart z \
        GROUP BY hour(str_to_date(start_time, '%c/%e/%Y %h:%i:%s %p'));"
    )
    res_str = json.dumps([dict(r) for r in res])
    return json.loads(res_str)
