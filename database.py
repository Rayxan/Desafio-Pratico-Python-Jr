from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
engine = create_engine("mysql+pymysql://root@localhost:3306/desafio")
 
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)