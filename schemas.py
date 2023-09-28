from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
 
# Create Nfe Schema (Pydantic Model)
# class NfeCreate(BaseModel):
#     chNFe: str
#     UF: str
#     cStat: str
#     mod: str
#     dhEmi: datetime
#     dhSaiEnt: datetime
#     tpNF: int
#     cMunFG: str
#     tpEmis: str
#     tpAmb: str
#     vBC: Decimal
#     vICMS: Decimal
#     vICMSDeson: Decimal
#     vBCST: Decimal
#     vST: Decimal
#     vProd: Decimal
#     vFrete: Decimal
#     vSeg: Decimal
#     vDesc: Decimal
#     vII: Decimal
#     vPIS: Decimal
#     vCOFINS: Decimal
#     vNF: Decimal
#     vTotTrib: Decimal
 
# Complete Nfe Schema (Pydantic Model)
class Nfe(BaseModel):
    id: int
    chNFe: str
    nProt: str
    UF: str
    cStat: str
    cNF: str
    natOp: str
    mod: str
    serie: str
    nNF: str
    dhEmi: datetime
    dhSaiEnt: datetime
    tpNF: int
    cMunFG: str
    tpEmis: str
    tpAmb: str
    vBC: Decimal
    vICMS: Decimal
    vICMSDeson: Decimal
    vBCST: Decimal
    vST: Decimal
    vProd: Decimal
    vFrete: Decimal
    vSeg: Decimal
    vDesc: Decimal
    vII: Decimal
    vPIS: Decimal
    vCOFINS: Decimal
    vNF: Decimal
    vTotTrib: Decimal
 
    class Config:
        orm_mode = True