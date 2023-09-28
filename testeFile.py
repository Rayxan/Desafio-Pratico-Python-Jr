from fastapi import FastAPI, UploadFile, File
from secrets import token_hex
import uvicorn
import xmltodict

app = FastAPI(title="Upload file")

@app.post("/upload")
async def upload(file:UploadFile = File(...)):
    with open(file.filename, 'r', encoding='utf-8') as xml_file:
        xml_data = xml_file.read()

    nfe_dict = xmltodict.parse(xml_data)
   
    nfe_numero = nfe_dict['nfeProc']['NFe']['infNFe']['ide']['nNF']

    return {"retorno": nfe_numero}


if __name__ == "__main__":
    uvicorn.run("testeFile:app", host='127.0.0.1', reload=True)

    