from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyodbc
from dotenv import load_dotenv
import os

# 🟢 Agregá esta línea justo después de los imports:
from app.routes import login
from app.routes import clientes

load_dotenv()

app = FastAPI()

# Configuración CORS

origins = [
    "http://localhost:5173",             # Para cuando lo corres en tu propia PC
    "http://192.168.100.132:5173",       # Para cuando accedes desde otros dispositivos con tu IP actual
    # "http://otrodominio.com",          # Si tu frontend estuviera en otro dominio
    # "https://otrodominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Leer variables del entorno
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DB")

# Función para conexión
def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
    )
    return conn

# Ruta de prueba
@app.get("/")
def root():
    return {"message": "API Lavandería funcionando correctamente"}

# 🟢 Agregá esta línea al final del archivo:
app.include_router(login.router)
app.include_router(clientes.router)

