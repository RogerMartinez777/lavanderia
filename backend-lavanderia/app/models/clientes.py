from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str
    apellido: str
    telefono: str
    mail: str
    nota: str

class ClienteCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: str
    mail: str
    nota: str
    

