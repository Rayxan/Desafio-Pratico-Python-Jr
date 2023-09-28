from pydantic import BaseModel
 
# Create Nfe Schema (Pydantic Model)
class NfeCreate(BaseModel):
    task: str
 
# Complete Nfe Schema (Pydantic Model)
class Nfe(BaseModel):
    id: int
    task: str
 
    class Config:
        orm_mode = True