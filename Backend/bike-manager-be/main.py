from fastapi import FastAPI 

from bike.TipoBike import TipoBike
from bike.persistencia.MockRepositorioBike import MockRepositorioBike as RepositorioBike

app = FastAPI() 

@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}

@app.get("/bikes")
def get_bikes(tipo: TipoBike = None, marchas: int = None, aro: int = None):
    print(f'Processando pesquisa por tipo: {tipo}, marchas: {marchas}, aro: {aro}')
    encontradas = RepositorioBike.find(tipo, marchas, aro)
    return encontradas

