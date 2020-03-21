from typing import List
from pydantic import BaseModel

class Complaint(BaseModel):
    sr_number : str
    sr_type_code : str
    sr_desc : str
    owning_dept : str
    method_received : str
    sr_status : str
    status_change_date : str
    created_date : str
    last_update_date : str
    close_date : str
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
            orm_mode = True

class Trip(BaseModel):
    trip_id : str
    vehicle_id : str
    vehicle_type : str
    trip_duration : int
    trip_distance : int
    start_time : str
    end_time : str
    modified_date : str
    council_dist_start : str
    council_dist_end : str
    year : int
    census_tract_start : str
    census_tract_end : str
    
    class Config:
            orm_mode = True
            
class ZipCode(BaseModel):
    census_tract : str
    zip_code : str
    population : int

    class Config:
            orm_mode = True