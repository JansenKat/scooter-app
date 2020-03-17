from typing import List
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

class Complaint(BaseModel):
    sr_number : str
    sr_type_code : str
    sr_desc : str
    owning_dept : str
    method_received : str
    sr_status : str
    status_change_date : datetime
    created_date : datetime
    last_update_date : datetime
    close_date : datetime
    sr_location : str
    street_number : str
    street_name : str
    city : str
    zip_code : str
    county : str
    x_coord : float
    y_coord : float
    latitude_coord : float
    longitude_coord : float
    lat_long : str
    council_district : str
    map_page : str
    map_tile : str

    class Config:
        orm_mode : True

class Trip(BaseModel):
    trip_id : str
    vehicle_id : str
    vehicle_type : str
    trip_duration : int
    trip_distance : int
    start_time : str
    end_time : str
    modified_date : datetime
    council_dist_start : str
    council_dist_end : str
    year : int
    census_tract_start : str
    census_tract_end : str

    class Config:
        orm_mode : True