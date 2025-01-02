from sqlalchemy import Column, Integer, String, Date, JSON
from app.database import Base

class SportType(Base):
    __tablename__ = "sport_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Athlete(Base):
    __tablename__ = "athlete"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birthdate = Column(Date)
    data = Column(JSON)

class Result(Base):
    __tablename__ = "result"
    id = Column(Integer, primary_key=True, index=True)
    athlete_id = Column(Integer)
    sport_type_id = Column(Integer)
    score = Column(String)
    event_date = Column(Date)

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
