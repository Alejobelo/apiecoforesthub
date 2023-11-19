from sqlalchemy import Column, Integer, String
from src.config import Base


class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(255))

    
