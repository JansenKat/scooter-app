from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String
from sqlalchemy.types import String

from .database import Base


class Complaint(Base):
    __tablename__ = "311_data"

    sr_number = Column(String, primary_key=True, index=True)
    sr_type_code = Column(String)
    sr_desc = Column(String)
    owning_dept = Column(String)
    method_received = Column(String)
    sr_status = Column(String)
    status_change_date = Column(String)
    created_date = Column(String)
    last_update_date = Column(String)
    close_date = Column(String)
    sr_location = Column(String)
    street_number = Column(String)
    street_name = Column(String)
    city = Column(String)
    zip_code = Column(String)
    county = Column(String)
    x_coord = Column(Float)
    y_coord = Column(Float)
    latitude_coord = Column(Float)
    longitude_coord = Column(Float)
    lat_long = Column(String)
    council_district = Column(String)
    map_page = Column(String)
    map_tile = Column(String)


class Trip(Base):
    __tablename__ = "scooter_2020"

    trip_id = Column(String, primary_key=True, index=True)
    trip_duration = Column(Float)
    trip_distance = Column(Float)
    start_time = Column(String)
    end_time = Column(String)
    start_zip = Column(String)
    end_zip = Column(String)
    startLat = Column(Float)
    endLat = Column(Float)
    startLon = Column(Float)
    endLon = Column(Float)


class ZipCode(Base):
    __tablename__ = "tract_to_zip"

    census_tract = Column(String, primary_key=True, index=True)
    zip_code = Column(String)
    population = Column(Integer)
