import os
import pyodbc
from dotenv import load_dotenv
from typing import Optional # <--- ¡NUEVA LÍNEA AÑADIDA AQUÍ!

load_dotenv()

# Carga las variables de entorno para la conexión a la base de datos
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DB")

def get_db_connection():
    """
    Establece y devuelve una conexión a la base de datos SQL Server.
    """
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;" # Usa autenticación de Windows
    )
    return conn

# 🟢 Funciones para la gestión de Clientes (existentes)
def obtener_clientes():
    """
    Obtiene todos los clientes de la base de datos.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, telefono, mail, nota FROM Clientes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": row[0], "nombre": row[1], "apellido": row[2], "telefono": row[3], "mail": row[4], "nota": row[5]} for row in rows]


def insertar_cliente(cliente):
    """
    Inserta un nuevo cliente en la base de datos.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Clientes (nombre, apellido, telefono, mail, nota) VALUES (?, ?, ?, ?, ?)",
        (cliente.nombre, cliente.apellido, cliente.telefono, cliente.mail, cliente.nota)
    )
    conn.commit()
    cursor.close()
    conn.close()

def obtener_cliente_por_id(cliente_id: int):
    """
    Obtiene un cliente por su ID de la base de datos.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, telefono, mail, nota FROM Clientes WHERE id = ?", cliente_id)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1], "apellido": row[2], "telefono": row[3], "mail": row[4], "nota": row[5]}
    return None

def actualizar_cliente_db(cliente_id: int, cliente_data):
    """
    Actualiza los datos de un cliente existente en la base de datos.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Clientes SET nombre = ?, apellido = ?, telefono = ?, mail = ?, nota = ? WHERE id = ?",
        (cliente_data.nombre, cliente_data.apellido, cliente_data.telefono, cliente_data.mail, cliente_data.nota, cliente_id)
    )
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0 # Retorna True si se actualizó, False si no se encontró

def eliminar_cliente_db(cliente_id: int):
    """
    Elimina un cliente de la base de datos por su ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", cliente_id)
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0 # Retorna True si se eliminó, False si no se encontró

# 🧺 Funciones para Acolchados y Precios (Nuevas)

# --- Categorias_Servicio ---
def obtener_categorias_servicio():
    """
    Obtiene todas las categorías de servicio disponibles (ej. Acolchados, Camperas).
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM Categorias_Servicio ORDER BY nombre")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Retorna una lista de diccionarios para facilitar el uso en la API
    return [{"id": row[0], "nombre": row[1]} for row in rows]

def obtener_categoria_servicio_por_id(categoria_id: int):
    """
    Obtiene una categoría de servicio por su ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM Categorias_Servicio WHERE id = ?", categoria_id)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1]}
    return None

def insertar_categoria_servicio(nombre: str):
    """
    Inserta una nueva categoría de servicio en la base de datos.
    Retorna el ID de la categoría insertada.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    # CAMBIO AQUÍ: Usar OUTPUT INSERTED.ID para obtener el ID directamente
    cursor.execute("INSERT INTO Categorias_Servicio (nombre) OUTPUT INSERTED.id VALUES (?)", nombre)
    new_id = cursor.fetchone()[0] # Obtener el ID del resultado de la inserción
    conn.commit()
    cursor.close()
    conn.close()
    return new_id # new_id ya debería ser un valor válido (Decimal o int)

def actualizar_categoria_servicio(categoria_id: int, nombre: str):
    """
    Actualiza el nombre de una categoría de servicio.
    Retorna True si se actualizó, False si no se encontró.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Categorias_Servicio SET nombre = ? WHERE id = ?", (nombre, categoria_id))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

def eliminar_categoria_servicio(categoria_id: int):
    """
    Elimina una categoría de servicio por su ID.
    Retorna True si se eliminó, False si no se encontró.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Categorias_Servicio WHERE id = ?", categoria_id)
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

# --- Tamanios ---
def obtener_tamanios():
    """
    Obtiene todos los tamaños disponibles (ej. 1 Plaza, 2 Plazas).
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM Tamanios ORDER BY nombre")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Retorna una lista de diccionarios
    return [{"id": row[0], "nombre": row[1]} for row in rows]

def obtener_tamanio_por_id(tamanio_id: int):
    """
    Obtiene un tamaño por su ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM Tamanios WHERE id = ?", tamanio_id)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        return {"id": row[0], "nombre": row[1]}
    return None

def insertar_tamanio(nombre: str):
    """
    Inserta un nuevo tamaño en la base de datos.
    Retorna el ID del tamaño insertado.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    # CAMBIO AQUÍ: Usar OUTPUT INSERTED.ID para obtener el ID directamente
    cursor.execute("INSERT INTO Tamanios (nombre) OUTPUT INSERTED.id VALUES (?)", nombre)
    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return new_id

def actualizar_tamanio(tamanio_id: int, nombre: str):
    """
    Actualiza el nombre de un tamaño.
    Retorna True si se actualizó, False si no se encontró.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Tamanios SET nombre = ? WHERE id = ?", (nombre, tamanio_id))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

def eliminar_tamanio(tamanio_id: int):
    """
    Elimina un tamaño por su ID.
    Retorna True si se eliminó, False si no se encontró.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tamanios WHERE id = ?", tamanio_id)
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

# --- Precios_Vigentes ---
def obtener_precios_vigentes():
    """
    Obtiene todos los precios vigentes, incluyendo los nombres de categoría y tamaño.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    # La consulta JOIN es la misma que usamos para verificar los datos
    cursor.execute("""
        SELECT
            pv.id,
            pv.categoria_id,
            cs.nombre AS categoria_nombre,
            pv.tamanio_id,
            t.nombre AS tamanio_nombre,
            pv.precio
        FROM
            Precios_Vigentes pv
        JOIN
            Categorias_Servicio cs ON pv.categoria_id = cs.id
        LEFT JOIN
            Tamanios t ON pv.tamanio_id = t.id
        ORDER BY
            cs.nombre, t.nombre;
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Formatea los resultados para que coincidan con el modelo PrecioVigente
    result = []
    for row in rows:
        precio_data = {
            "id": row[0],
            "categoria_id": row[1],
            "categoria": {"id": row[1], "nombre": row[2]}, # Anida el objeto Categoría
            "tamanio_id": row[3],
            "precio": float(row[5]) # Asegura que el precio sea float
        }
        if row[3] is not None: # Si tiene tamaño, anida el objeto Tamaño
            precio_data["tamanio"] = {"id": row[3], "nombre": row[4]}
        else:
            precio_data["tamanio"] = None # Asegura que sea None si no hay tamaño
        result.append(precio_data)
    return result

def obtener_precio_vigente(categoria_id: int, tamanio_id: Optional[int] = None):
    """
    Obtiene el precio vigente para una combinación específica de categoría y tamaño.
    Si el tamaño_id es None, busca precios para categorías sin tamaño.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    if tamanio_id is None:
        cursor.execute(
            "SELECT pv.id, pv.categoria_id, pv.tamanio_id, pv.precio FROM Precios_Vigentes pv WHERE pv.categoria_id = ? AND pv.tamanio_id IS NULL",
            categoria_id
        )
    else:
        cursor.execute(
            "SELECT pv.id, pv.categoria_id, pv.tamanio_id, pv.precio FROM Precios_Vigentes pv WHERE pv.categoria_id = ? AND pv.tamanio_id = ?",
            (categoria_id, tamanio_id)
        )
    
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        # Devuelve solo el valor del precio para el endpoint específico
        return float(row[3]) # Asegura que el precio sea float
    return None

def obtener_precio_vigente_por_id(precio_id: int):
    """
    Obtiene un precio vigente por su ID, incluyendo los nombres de categoría y tamaño.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            pv.id,
            pv.categoria_id,
            cs.nombre AS categoria_nombre,
            pv.tamanio_id,
            t.nombre AS tamanio_nombre,
            pv.precio
        FROM
            Precios_Vigentes pv
        JOIN
            Categorias_Servicio cs ON pv.categoria_id = cs.id
        LEFT JOIN
            Tamanios t ON pv.tamanio_id = t.id
        WHERE
            pv.id = ?;
    """, precio_id)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    if row:
        precio_data = {
            "id": row[0],
            "categoria_id": row[1],
            "categoria": {"id": row[1], "nombre": row[2]},
            "tamanio_id": row[3],
            "precio": float(row[5])
        }
        if row[3] is not None:
            precio_data["tamanio"] = {"id": row[3], "nombre": row[4]}
        else:
            precio_data["tamanio"] = None
        return precio_data
    return None

def insertar_precio_vigente(categoria_id: int, tamanio_id: Optional[int], precio: float):
    """
    Inserta un nuevo precio vigente en la base de datos.
    Retorna el ID del precio insertado.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    # CAMBIO AQUÍ: Usar OUTPUT INSERTED.ID para obtener el ID directamente
    cursor.execute(
        "INSERT INTO Precios_Vigentes (categoria_id, tamanio_id, precio) OUTPUT INSERTED.id VALUES (?, ?, ?)",
        (categoria_id, tamanio_id, precio)
    )
    new_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return new_id


def actualizar_precio_vigente(precio_id: int, categoria_id: Optional[int] = None, tamanio_id: Optional[int] = None, precio: Optional[float] = None):
    """
    Actualiza un precio vigente existente. Permite actualizaciones parciales.
    Retorna True si se actualizó, False si no se encontró o no hubo cambios.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Construir la consulta UPDATE dinámicamente
    updates = []
    params = []

    if categoria_id is not None:
        updates.append("categoria_id = ?")
        params.append(categoria_id)

# 📝 Próximas funciones a implementar: Alta de Lavados y Detalle_Lavado
# def insertar_lavado(lavado_data):
#     pass

# def insertar_detalle_lavado(detalle_data):
#     pass