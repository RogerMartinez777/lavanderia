from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import get_db_connection

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(data: LoginData):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT COUNT(*) FROM Usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, data.username, data.password)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result and result[0] == 1:
        return {"message": "Login exitoso", "token": "fake-jwt-token"}
    
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
