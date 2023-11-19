from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user='root'
password='h42wfhnf'
host='localhost'
port='3306'
data_base='ecoforesthub'

database_url=f"mysql://{user}:{password}@{host}:{port}/{data_base}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

