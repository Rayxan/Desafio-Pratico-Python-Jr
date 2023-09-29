# Teste para Desenvolvedor Júnior Python

## Descrição

O objetivo deste teste é avaliar sua habilidade em desenvolver uma API REST usando FastAPI, realizar o processamento de arquivos XML (Nota Fiscal Eletrônica - NFE), e persistir os dados em um banco.

### Funcionalidades

1. **Endpoint de Upload (POST /upload/)**
    - Permitir o upload de arquivos XML (NFE).
    - Realizar o processamento e extração dos dados relevantes do XML.
    - Validar o XML de entrada (certificar-se de que é uma NFE válida).

2. **Endpoints de Consulta Lista (GET /nfe/)**
    - Listagem de todas as NFes carregadas.

3. **Endpoints de Consulta ID(GET /nfe/{nfe_id})**
    - Exibição de detalhes específicos de uma NFE, buscada pelo seu ID ou chave de acesso.
    - Na implementação em questão, a consulta é a através da `chNFe` da nota.

## Pré-requisitos

* Python >= 3.8

## Instruções para configuração do ambiente

No seu terminal rode o seguinte comando
```
pip install -r requirements.txt
```
Acesse o arquivo database.py e configure suas credenciais de banco mysql, e crie um banco chamado `desafio`.
```python
# database.py
engine = create_engine("mysql+pymysql://root@localhost:3306/desafio")
```
Em seguida rode o seguinte comando para colocar a aplicação no ar.
```
uvicorn main:app --reload
```
Acesse a aplicação em:
```
localhost:8000/docs
```
