from pydantic import BaseModel, Field
from typing import Optional # esto permite que un campo sea int o nulo (tamanio_id)

# Configuración base para los modelos Pydantic
# Permite que los modelos se creen a partir de atributos de objetos ORM
# (útil cuando se obtienen datos directamente de la base de datos)
class Config:
    orm_mode = True
    # Permite que los campos sean accesibles por nombre de atributo (ej. row.id)
    # en lugar de solo por clave de diccionario (ej. row['id'])
    # También permite la conversión de tipos de datos de la base de datos a tipos Python.
    from_attributes = True


# --- Modelos para Categorias_Servicio ---
class CategoriaServicioBase(BaseModel):
    """
    Modelo base para una categoría de servicio.
    Define los campos comunes para creación y respuesta.
    """
    nombre: str = Field(..., max_length=50, description="Nombre de la categoría de servicio (ej. Acolchados, Camperas)")

class CategoriaServicioCreate(CategoriaServicioBase):
    """
    Modelo para la creación de una nueva categoría de servicio.
    Hereda de CategoriaServicioBase.
    """
    pass # No se necesitan campos adicionales para la creación, solo el nombre

class CategoriaServicio(CategoriaServicioBase):
    """
    Modelo para la respuesta de una categoría de servicio, incluyendo su ID.
    """
    id: int = Field(..., description="ID único de la categoría de servicio")

    class Config(Config):
        """Configuración Pydantic para este modelo."""
        pass


# --- Modelos para Tamanios ---
class TamanioBase(BaseModel):
    """
    Modelo base para un tamaño.
    Define los campos comunes para creación y respuesta.
    """
    nombre: str = Field(..., max_length=50, description="Nombre del tamaño (ej. 1 Plaza, 2 Plazas)")

class TamanioCreate(TamanioBase):
    """
    Modelo para la creación de un nuevo tamaño.
    Hereda de TamanioBase.
    """
    pass # No se necesitan campos adicionales para la creación, solo el nombre

class Tamanio(TamanioBase):
    """
    Modelo para la respuesta de un tamaño, incluyendo su ID.
    """
    id: int = Field(..., description="ID único del tamaño")

    class Config(Config):
        """Configuración Pydantic para este modelo."""
        pass


# --- Modelos para Precios_Vigentes ---
class PrecioVigenteBase(BaseModel):
    """
    Modelo base para un precio vigente.
    Define los campos comunes para creación y actualización.
    """
    categoria_id: int = Field(..., description="ID de la categoría de servicio a la que aplica el precio")
    tamanio_id: Optional[int] = Field(None, description="ID del tamaño al que aplica el precio (opcional, NULL si no aplica)")
    precio: float = Field(..., gt=0, description="El precio vigente para la combinación de categoría y tamaño")

class PrecioVigenteCreate(PrecioVigenteBase):
    """
    Modelo para la creación de un nuevo precio vigente.
    Hereda de PrecioVigenteBase.
    """
    pass # No se necesitan campos adicionales para la creación

class PrecioVigenteUpdate(PrecioVigenteBase):
    """
    Modelo para la actualización de un precio vigente.
    Todos los campos son opcionales para permitir actualizaciones parciales.
    """
    categoria_id: Optional[int] = Field(None, description="ID de la categoría de servicio a la que aplica el precio")
    tamanio_id: Optional[int] = Field(None, description="ID del tamaño al que aplica el precio (opcional, NULL si no aplica)")
    precio: Optional[float] = Field(None, gt=0, description="El precio vigente para la combinación de categoría y tamaño")

class PrecioVigente(PrecioVigenteBase):
    """
    Modelo para la respuesta de un precio vigente, incluyendo su ID.
    También incluye los objetos de Categoría y Tamaño anidados para una respuesta más completa.
    """
    id: int = Field(..., description="ID único del precio vigente")
    categoria: CategoriaServicio = Field(..., description="Detalles de la categoría de servicio")
    tamanio: Optional[Tamanio] = Field(None, description="Detalles del tamaño (opcional)")

    class Config(Config):
        """Configuración Pydantic para este modelo."""
        pass

