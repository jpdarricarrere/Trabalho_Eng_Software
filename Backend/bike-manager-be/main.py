from fastapi import FastAPI 

from bike.TipoBike import TipoBike
from bike.persistencia.MockRepositorioBike import MockRepositorioBike

app = FastAPI() 

@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}

@app.get("/bikes")
def get_bikes(tipo: TipoBike = None, marchas: int = None, aro: int = None):
    print(f'Searched for tipo: {tipo}, marchas: {marchas}, aro: {aro}')
    return [MockRepositorioBike.find()]