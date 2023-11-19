from typing import List
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from src.models.query.query import QueryModel
from fastapi.responses import JSONResponse
from src.config import Session, engine, Base
from src.config.schemas.query import Query
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from src.routes.auth.auth import auth_router
from src.routes.query.query import query_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.title='API-Ecoforesthub'

app.add_middleware(ErrorHandler)
origins = [
    "http://localhost",        # Origen para desarrollo local
    "http://localhost:4200",   # Origen del frontend en el puerto 4200
    "https://tufrontend.com",  # Reemplaza esto con el dominio real de tu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],      # Permite todos los métodos HTTP
    allow_headers=["*"],      # Permite todos los encabezados HTTP
)
app.include_router(auth_router)
app.include_router(query_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Welcome</h1>')




