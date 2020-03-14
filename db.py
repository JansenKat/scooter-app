from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = "mysql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DictMixIn:
    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            if not isinstance(getattr(self, column.name), dt.datetime)
            else getattr(self, column.name).isoformat()
            for column in self.__table__.columns
        }

class Complaint(Base, DictMixIn):
    __tablename__ = "users"
    sr_number = Column(String, primary_key=True)
    sr_type_code = Column(String)
    sr_desc = Column(String)
    owning_dept = Column(String)
    method_received = Column(String)
    sr_status = Column(String)
    status_change_date = Column(DateTime)
    created_date = Column(DateTime)
    last_update_date = Column(DateTime)
    close_date = Column(DateTime)
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

    items = relationship("Item", back_populates="owner")

class Scooter_Trip(Base, DictMixIn):
    __tablename__ = "items"

    trip_id = Column(String, primary_key=True)
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

    owner = relationship("User", back_populates="items")

