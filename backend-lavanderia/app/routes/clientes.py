from fastapi import APIRouter, HTTPException, status # <-- Aquí falta 'status'
from app.models.clientes import ClienteCreate, Cliente
from app.db import obtener_clientes, insertar_cliente, obtener_cliente_por_id, actualizar_cliente_db, eliminar_cliente_db

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("")
def listar_clientes():
    rows = obtener_clientes()
    clientes = []
    for row in rows:
        clientes.append({
            "id": row[0],
            "nombre": row[1],
            "apellido": row[2],
            "telefono": row[3],
            "mail": row[4],
            "nota": row[5]
        })
    return clientes

@router.post("")
def crear_cliente(cliente: ClienteCreate):
    insertar_cliente(cliente)
    return {"mensaje": "Cliente creado exitosamente"}

# 🟢 Obtener un cliente por su ID
@router.get("/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    row = obtener_cliente_por_id(cliente_id)
    if row:
        return Cliente(
            id=row[0],
            nombre=row[1],
            apellido=row[2],
            telefono=row[3],
            mail=row[4],
            nota=row[5]
        )
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# 🟢 NUEVA RUTA: Actualizar un cliente
@router.put("/{cliente_id}", response_model=Cliente) # Retorna el cliente actualizado
def actualizar_cliente(cliente_id: int, cliente: ClienteCreate): # Usa ClienteCreate para la entrada
    # Primero, verifica si el cliente existe
    existing_cliente_row = obtener_cliente_por_id(cliente_id)
    if not existing_cliente_row:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Actualiza el cliente en la base de datos
    actualizar_cliente_db(cliente_id, cliente)

    # Opcional: Obtener y devolver el cliente actualizado para confirmación
    updated_cliente_row = obtener_cliente_por_id(cliente_id)
    if updated_cliente_row:
         return Cliente(
            id=updated_cliente_row[0],
            nombre=updated_cliente_row[1],
            apellido=updated_cliente_row[2],
            telefono=updated_cliente_row[3],
            mail=updated_cliente_row[4],
            nota=updated_cliente_row[5]
        )
    # Esto no debería ocurrir si el update fue exitoso, pero es un fallback
    raise HTTPException(status_code=500, detail="Error al recuperar cliente actualizado")


# 🟢 Eliminar un cliente por su ID
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT) # No Content si la eliminación fue exitosa
def eliminar_cliente(cliente_id: int):
    try:
        eliminar_cliente_db(cliente_id)
        return {"message": "Cliente eliminado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar cliente: {e}")