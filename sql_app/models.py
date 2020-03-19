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
    __tablename__ = "scooter_data"

    trip_id = Column(String, primary_key=True, index=True)
    vehicle_id = Column(String)
    vehicle_type = Column(String)
    trip_duration = Column(Integer)
    trip_distance = Column(Integer)
    start_time = Column(String)
    end_time = Column(String)
    modified_date = Column(String)
    council_dist_start = Column(String)
    council_dist_end = Column(String)
    year = Column(Integer)
    census_tract_start = Column(String)
    census_tract_end = Column(String)

