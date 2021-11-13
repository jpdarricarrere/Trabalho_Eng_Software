from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from bike.api import router as bike_router
from usuario.api import router as usuario_router

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

@app.get("/")
def server_status_index():
    return {"Status": "It lives!"}

