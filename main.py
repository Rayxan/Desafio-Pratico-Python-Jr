from typing import List
from fastapi import FastAPI, status, HTTPException, Depends, UploadFile, File
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
import xmltodict
import xmlschema
from lxml import etree
 
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

@app.get("/nfe/", response_model=List[schemas.Nfe])
def read_nfes(session: Session = Depends(get_session)):
    nfes = session.query(models.Nfe).all()
    return nfes

@app.get("/nfe/{nfe_id}")
def get_nfe_details(nfe_id: int, session: Session = Depends(get_session)):
    nfe = session.query(models.Nfe).filter(models.Nfe.id == nfe_id).first()

    if not nfe:
        raise HTTPException(status_code=404, detail="NFE não encontrada")
    return nfe

@app.post("/upload/", status_code=status.HTTP_201_CREATED)
async def upload(file:UploadFile = File(...), session: Session = Depends(get_session)):
    try:
        xml_data = await file.read()

        #validação
        xml_root = etree.fromstring(xml_data)

        nfe_dict = xmltodict.parse(xml_data)

        nfe_info = nfe_dict['nfeProc']['NFe']['infNFe']

        nfe_numero = nfe_info['ide']['nNF']
        nProt = nfe_dict['nfeProc']['protNFe']['infProt']['nProt']
        UF = nfe_dict['nfeProc']['protNFe']['infProt']['tpAmb']
        cStat = nfe_dict['nfeProc']['protNFe']['infProt']['cStat']
        cNF = nfe_info['ide']['cNF']
        natOp = nfe_info['ide']['natOp']
        mod = nfe_info['ide']['mod']
        serie = nfe_info['ide']['serie']
        dhEmi = nfe_info['ide']['dhEmi']
        dhSaiEnt = nfe_info['ide'].get('dhSaiEnt')
        tpNF = nfe_info['ide']['tpNF']
        cMunFG = nfe_info['ide']['cMunFG']
        tpEmis = nfe_info['ide']['tpEmis']
        tpAmb = nfe_info['ide']['tpAmb']
        vBC = nfe_info['total']['ICMSTot']['vBC']
        vICMS = nfe_info['total']['ICMSTot']['vICMS']
        vICMSDeson = nfe_info['total']['ICMSTot']['vICMSDeson']
        vBCST = nfe_info['total']['ICMSTot']['vBCST']
        vST = nfe_info['total']['ICMSTot']['vST']
        vProd = nfe_info['total']['ICMSTot']['vProd']
        vFrete = nfe_info['total']['ICMSTot']['vFrete']
        vSeg = nfe_info['total']['ICMSTot']['vSeg']
        vDesc = nfe_info['total']['ICMSTot']['vDesc']
        vII = nfe_info['total']['ICMSTot']['vII']
        vPIS = nfe_info['total']['ICMSTot']['vPIS']
        vCOFINS = nfe_info['total']['ICMSTot']['vCOFINS']
        vNF = nfe_info['total']['ICMSTot']['vNF']
        vTotTrib = nfe_info['total']['ICMSTot']['vTotTrib']

        nfedb = models.Nfe(
            chNFe=nfe_numero,
            nProt=nProt,
            UF=UF,
            cStat=cStat,
            cNF=cNF,
            natOp=natOp,
            mod=mod,
            serie=serie,
            nNF=nfe_numero,
            dhEmi=dhEmi,
            dhSaiEnt=dhSaiEnt,
            tpNF=tpNF,
            cMunFG=cMunFG,
            tpEmis=tpEmis,
            tpAmb=tpAmb,
            vBC=vBC,
            vICMS=vICMS,
            vICMSDeson=vICMSDeson,
            vBCST=vBCST,
            vST=vST,
            vProd=vProd,
            vFrete=vFrete,
            vSeg=vSeg,
            vDesc=vDesc,
            vII=vII,
            vPIS=vPIS,
            vCOFINS=vCOFINS,
            vNF=vNF,
            vTotTrib=vTotTrib
        )

        # Add the new Nfe item to the database
        session.add(nfedb)
        session.commit()
        session.refresh(nfedb)

        return {"message": "NFe processada e salva com sucesso"}

    except:
        raise HTTPException(status_code=400, detail=f"XML NFE inválida")
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=f"Erro ao processar o XML: {str(e)}")

   
