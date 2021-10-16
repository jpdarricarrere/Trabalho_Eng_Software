from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from bike.TipoBike import TipoBike
from bike.persistencia.MockRepositorioBike import MockRepositorioBike as RepositorioBike

app = FastAPI() 
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}

@app.get("/bikes")
def get_bikes(tipo: TipoBike = None, nome: str = "", modelo: str = "", marchas: int = None, aro: int = None):
    print(f'Processando pesquisa por tipo: {tipo}, nome: {nome}, marchas: {marchas}, aro: {aro}')
    encontradas = RepositorioBike.find(tipo, nome, modelo, marchas, aro)
    return encontradas

