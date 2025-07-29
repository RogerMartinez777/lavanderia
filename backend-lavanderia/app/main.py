from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyodbc
from dotenv import load_dotenv
import os

# 🟢 Agregá esta línea justo después de los imports:
from app.routes import login
from app.routes import clientes
from app.routes import servicios

load_dotenv()

app = FastAPI()

# Configuración CORS
# Es importante que el allow_origins incluya la IP de tu PC para acceso desde otros dispositivos
origins = [
    "http://localhost:5173",             # Para cuando lo corres en tu propia PC
    "http://192.168.100.132:5173",       # Para cuando accedes desde otros dispositivos con tu IP actual
    # "http://otrodominio.com",          # Si tu frontend estuviera en otro dominio
    # "https://otrodominio.com",
]

app.add_middleware(
    CORSMiddleware,
    # Se recomienda ser más específico con allow_origins en producción
    # Pero para desarrollo, "*" es común para evitar problemas de CORS.
    allow_origins=["*"], # Permite todas las IPs y dominios para desarrollo
    allow_credentials=True,
    allow_methods=["*"], # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permite todos los encabezados
)

# Leer variables del entorno
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DB")

# Función para conexión (aunque ya la tienes en db.py, aquí solo la defines si la usaras directamente en main.py)
# Si no la usas aquí, podrías considerar eliminarla de main.py para evitar duplicidad,
# ya que db.py es el módulo encargado de la gestión de la conexión.
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

# 🟢 Incluye los routers en la aplicación FastAPI
app.include_router(login.router)
app.include_router(clientes.router)
app.include_router(servicios.router)

