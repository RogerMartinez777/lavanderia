from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Optional

# Importa las funciones de acceso a la base de datos
from app import db

# Importa los modelos Pydantic que definimos
from app.models.servicios import (
    CategoriaServicio, CategoriaServicioCreate,
    Tamanio, TamanioCreate,
    PrecioVigente, PrecioVigenteCreate, PrecioVigenteUpdate
)

# Crea una instancia de APIRouter para agrupar las rutas de servicios
router = APIRouter(
    prefix="/servicios", # Prefijo para todas las rutas en este archivo (ej. /servicios/categorias)
    tags=["Servicios y Precios"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "No encontrado"}},
)

# --- Endpoints para Categorias_Servicio ---

@router.get("/categorias/", response_model=List[CategoriaServicio])
async def get_categorias_servicio():
    """
    Obtiene todas las categorías de servicio disponibles.
    """
    categorias = db.obtener_categorias_servicio()
    if not categorias:
        raise HTTPException(status_code=404, detail="No se encontraron categorías de servicio.")
    return categorias

@router.get("/categorias/{categoria_id}", response_model=CategoriaServicio)
async def get_categoria_servicio_by_id(categoria_id: int):
    """
    Obtiene una categoría de servicio por su ID.
    """
    categoria = db.obtener_categoria_servicio_por_id(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail=f"Categoría de servicio con ID {categoria_id} no encontrada.")
    return categoria

@router.post("/categorias/", response_model=CategoriaServicio, status_code=status.HTTP_201_CREATED)
async def create_categoria_servicio(categoria: CategoriaServicioCreate):
    """
    Crea una nueva categoría de servicio.
    """
    try:
        new_id = db.insertar_categoria_servicio(categoria.nombre)
        # Retorna la categoría recién creada con su ID
        return {"id": new_id, "nombre": categoria.nombre}
    except Exception as e:
        # Aquí puedes manejar errores específicos de la DB, como duplicados si el nombre es UNIQUE
        raise HTTPException(status_code=400, detail=f"Error al crear categoría de servicio: {e}")

@router.put("/categorias/{categoria_id}", response_model=CategoriaServicio)
async def update_categoria_servicio(categoria_id: int, categoria: CategoriaServicioCreate):
    """
    Actualiza el nombre de una categoría de servicio existente.
    """
    updated = db.actualizar_categoria_servicio(categoria_id, categoria.nombre)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Categoría de servicio con ID {categoria_id} no encontrada.")
    # Retorna la categoría actualizada
    return {"id": categoria_id, "nombre": categoria.nombre}

@router.delete("/categorias/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_categoria_servicio(categoria_id: int):
    """
    Elimina una categoría de servicio por su ID.
    """
    deleted = db.eliminar_categoria_servicio(categoria_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Categoría de servicio con ID {categoria_id} no encontrada.")
    return # No se devuelve contenido para 204 No Content

# --- Endpoints para Tamanios ---

@router.get("/tamanios/", response_model=List[Tamanio])
async def get_tamanios():
    """
    Obtiene todos los tamaños disponibles.
    """
    tamanios = db.obtener_tamanios()
    if not tamanios:
        raise HTTPException(status_code=404, detail="No se encontraron tamaños.")
    return tamanios

@router.get("/tamanios/{tamanio_id}", response_model=Tamanio)
async def get_tamanio_by_id(tamanio_id: int):
    """
    Obtiene un tamaño por su ID.
    """
    tamanio = db.obtener_tamanio_por_id(tamanio_id)
    if not tamanio:
        raise HTTPException(status_code=404, detail=f"Tamaño con ID {tamanio_id} no encontrado.")
    return tamanio

@router.post("/tamanios/", response_model=Tamanio, status_code=status.HTTP_201_CREATED)
async def create_tamanio(tamanio: TamanioCreate):
    """
    Crea un nuevo tamaño.
    """
    try:
        new_id = db.insertar_tamanio(tamanio.nombre)
        return {"id": new_id, "nombre": tamanio.nombre}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear tamaño: {e}")

@router.put("/tamanios/{tamanio_id}", response_model=Tamanio)
async def update_tamanio(tamanio_id: int, tamanio: TamanioCreate): # Reutilizamos TamanioCreate para la entrada
    """
    Actualiza el nombre de un tamaño existente.
    """
    updated = db.actualizar_tamanio(tamanio_id, tamanio.nombre)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Tamaño con ID {tamanio_id} no encontrado.")
    return {"id": tamanio_id, "nombre": tamanio.nombre}

@router.delete("/tamanios/{tamanio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tamanio(tamanio_id: int):
    """
    Elimina un tamaño por su ID.
    """
    deleted = db.eliminar_tamanio(tamanio_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Tamaño con ID {tamanio_id} no encontrado.")
    return # No se devuelve contenido para 204 No Content

# --- Endpoints para Precios_Vigentes ---

@router.get("/precios_vigentes/", response_model=List[PrecioVigente])
async def get_precios_vigentes_all():
    """
    Obtiene todos los precios vigentes registrados, con detalles de categoría y tamaño.
    """
    precios = db.obtener_precios_vigentes()
    if not precios:
        raise HTTPException(status_code=404, detail="No se encontraron precios vigentes.")
    return precios

@router.get("/precios_vigentes/buscar", response_model=float)
async def get_precio_vigente_by_params(
    categoria_id: int = Query(..., description="ID de la categoría de servicio"),
    tamanio_id: Optional[int] = Query(None, description="ID del tamaño (opcional para ítems sin tamaño)")
):
    """
    Obtiene el precio vigente para una combinación específica de categoría y tamaño.
    Si el tamaño no aplica para la categoría (ej. Camperas), no se debe proporcionar tamanio_id.
    """
    precio = db.obtener_precio_vigente(categoria_id, tamanio_id)
    if precio is None:
        raise HTTPException(status_code=404, detail="Precio no encontrado para la combinación de categoría y tamaño especificada.")
    return precio

@router.get("/precios_vigentes/{precio_id}", response_model=PrecioVigente)
async def get_precio_vigente_by_id(precio_id: int):
    """
    Obtiene un precio vigente por su ID.
    """
    precio = db.obtener_precio_vigente_por_id(precio_id)
    if not precio:
        raise HTTPException(status_code=404, detail=f"Precio vigente con ID {precio_id} no encontrado.")
    return precio

@router.post("/precios_vigentes/", response_model=PrecioVigente, status_code=status.HTTP_201_CREATED)
async def create_precio_vigente(precio_data: PrecioVigenteCreate):
    """
    Crea un nuevo precio vigente.
    """
    try:
        new_id = db.insertar_precio_vigente(
            precio_data.categoria_id,
            precio_data.tamanio_id,
            precio_data.precio
        )
        # Obtener el objeto completo para la respuesta
        new_precio = db.obtener_precio_vigente_por_id(new_id)
        if not new_precio: # Fallback si no se puede obtener justo después de insertar
            raise HTTPException(status_code=500, detail="Error al recuperar el precio recién creado.")
        return new_precio
    except Exception as e:
        # Aquí puedes manejar errores específicos de la DB, como la restricción UNIQUE
        raise HTTPException(status_code=400, detail=f"Error al crear precio vigente: {e}")

@router.put("/precios_vigentes/{precio_id}", response_model=PrecioVigente)
async def update_precio_vigente(precio_id: int, precio_data: PrecioVigenteUpdate):
    """
    Actualiza un precio vigente existente. Permite actualizaciones parciales.
    """
    updated = db.actualizar_precio_vigente(
        precio_id,
        precio_data.categoria_id,
        precio_data.tamanio_id,
        precio_data.precio
    )
    if not updated:
        # Si no se actualizó, puede ser que no se encontró o no hubo cambios
        # Intentamos obtenerlo para ver si existe y no hubo cambios, o si realmente no existe
        existing_precio = db.obtener_precio_vigente_por_id(precio_id)
        if not existing_precio:
            raise HTTPException(status_code=404, detail=f"Precio vigente con ID {precio_id} no encontrado.")
        # Si existe pero no se actualizó, es porque los datos enviados eran los mismos
        return existing_precio # Devolvemos el estado actual del recurso
    
    # Si se actualizó, obtenemos el recurso actualizado para la respuesta
    updated_precio = db.obtener_precio_vigente_por_id(precio_id)
    if not updated_precio: # Esto no debería pasar si 'updated' es True
        raise HTTPException(status_code=500, detail="Error al recuperar el precio actualizado.")
    return updated_precio

@router.delete("/precios_vigentes/{precio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_precio_vigente(precio_id: int):
    """
    Elimina un precio vigente por su ID.
    """
    deleted = db.eliminar_precio_vigente(precio_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Precio vigente con ID {precio_id} no encontrado.")
    return # No se devuelve contenido para 204 No Content
