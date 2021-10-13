from fastapi import FastAPI 

from bicicleta.TipoBicicleta import TipoBicicleta

app = FastAPI() 

@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}

@app.get("/bicicletas")
def get_bicicletas(tipo: TipoBicicleta = None, marchas: int = None, aro: int = None):
    print(f'Searched for tipo: {tipo}, marchas: {marchas}, aro: {aro}')
    return []