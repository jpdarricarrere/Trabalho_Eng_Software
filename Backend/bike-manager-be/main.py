from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from servico.api import router as bike_router, servico as servico_bike
from usuario.api import router as usuario_router
from emprestimo.api import router as emprestimo_router, servico as servico_emprestimo

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bike_router)
app.include_router(usuario_router)
app.include_router(emprestimo_router)


@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}


# Injecao de dependencias
servico_emprestimo.set_servico_bike(servico_bike)
