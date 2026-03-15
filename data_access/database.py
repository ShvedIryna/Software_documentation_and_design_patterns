from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_access.models import Base

engine = create_engine("sqlite:///financial.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

def init_db():
    Base.metadata.create_all(engine)