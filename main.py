from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, UploadFile, File
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import xmltodict
import xmlschema
 
Base.metadata.create_all(engine) # Create the database
 
# Initialize app
app = FastAPI()
 
# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
 
@app.get("/")
def root():
    return "nfes"
 
@app.post("/nfe", response_model=schemas.Nfe, status_code=status.HTTP_201_CREATED)
def create_nfe(nfe: schemas.NfeCreate, session: Session = Depends(get_session)):
 
    nfedb = models.Nfe(task = nfe.task)
 
    session.add(nfedb)
    session.commit()
    session.refresh(nfedb)
 
    return nfedb
 
@app.get("/nfe/{id}", response_model=schemas.Nfe)
def read_nfe(id: int, session: Session = Depends(get_session)):
 
    nfe = session.query(models.Nfe).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not nfe:
        raise HTTPException(status_code=404, detail=f"nfe item with id {id} not found")
 
    return nfe
 
@app.put("/nfe/{id}", response_model=schemas.Nfe)
def update_nfe(id: int, task: str, session: Session = Depends(get_session)):
 
    nfe = session.query(models.Nfe).get(id)     # get given id
 
    if nfe:
        nfe.task = task
        session.commit()
 
    # check if id exists. If not, return 404 not found response
    if not nfe:
        raise HTTPException(status_code=404, detail=f"nfe item with id {id} not found")
 
    return nfe
 
@app.delete("/nfe/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_nfe(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    nfe = session.query(models.Nfe).get(id)
 
    # if nfe item with given id exists, delete it from the database. Otherwise raise 404 error
    if nfe:
        session.delete(nfe)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"nfe item with id {id} not found")
 
    return None
 
@app.get("/nfe", response_model = List[schemas.Nfe])
def read_nfe_list(session: Session = Depends(get_session)):
 
    nfe_list = session.query(models.Nfe).all() # get all nfe items
 
    return nfe_list  

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload(file:UploadFile = File(...), session: Session = Depends(get_session)):
    with open(file.filename, 'r', encoding='utf-8') as xml_file:
        xml_data = xml_file.read()

    nfe_dict = xmltodict.parse(xml_data)

    nfe_numero = nfe_dict['nfeProc']['NFe']['infNFe']['ide']['nNF']

    nfedb = models.Nfe(task=nfe_numero)

    # Add the new Nfe item to the database
    session.add(nfedb)
    session.commit()
    session.refresh(nfedb)

    return {"message": "NFe processada e salva com sucesso"}

   
