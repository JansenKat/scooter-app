from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String 
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

class User(Base, DictMixIn):
    __tablename__ = "users"

    items = relationship("Item", back_populates="owner")

class Item(Base, DictMixIn):
    __tablename__ = "items"

    owner = relationship("User", back_populates="items")

