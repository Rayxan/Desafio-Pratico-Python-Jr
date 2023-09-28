from sqlalchemy import Column, Integer, String
from database import Base
 
# Define Nfe class from Base
class Nfe(Base):
    __tablename__ = 'nfes'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))