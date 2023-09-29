# Teste para Desenvolvedor JÃºnior Python

## DescriÃ§Ã£o

O objetivo deste teste Ã© avaliar sua habilidade em desenvolver uma API REST usando FastAPI, realizar o processamento de arquivos XML (Nota Fiscal EletrÃ´nica - NFE), e persistir os dados em um banco.

### Funcionalidades

1. **Endpoint de Upload (POST /upload/)**
    - Permitir o upload de arquivos XML (NFE).
    - Realizar o processamento e extraÃ§Ã£o dos dados relevantes do XML.
    - Validar o XML de entrada (certificar-se de que Ã© uma NFE vÃ¡lida).

2. **Endpoints de Consulta Lista (GET /nfe/)**
    - Listagem de todas as NFes carregadas.

3. **Endpoints de Consulta ID(GET /nfe/{nfe_id})**
    - ExibiÃ§Ã£o de detalhes especÃ­ficos de uma NFE, buscada pelo seu ID ou chave de acesso.


## PrÃ©-requisitos

* Python >= 3.8

## InstruÃ§Ãµes para configuraÃ§Ã£o do ambiente

No seu terminal rode o seguinte comando
```
pip install -r requirements.txt
```
Acesse o arquivo database.py e configure suas credenciais de banco mysql, e crie um banco chamado `desafio`.
```
# database.py
engine = create_engine("mysql+pymysql://root@localhost:3306/desafio")
```
Em seguida rode o seguinte comando para colocar a aplicaÃ§Ã£o no ar.
```
uvicorn main:app --reload
```
Acesse a aplicaÃ§Ã£o em:
```
localhost:8000/docs
```