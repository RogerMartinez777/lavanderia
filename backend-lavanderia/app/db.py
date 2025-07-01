import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DB")

def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
    )
    return conn

# 🟢 Obtener todos los clientes
def obtener_clientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, telefono, mail, nota FROM Clientes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# 🟢 Insertar un nuevo cliente
def insertar_cliente(cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Clientes (nombre, apellido, telefono, mail, nota) VALUES (?, ?, ?, ?, ?)",
        (cliente.nombre, cliente.apellido, cliente.telefono, cliente.mail, cliente.nota)
    )
    conn.commit()
    cursor.close()
    conn.close()

# 🟢 Obtener un cliente por su ID
def obtener_cliente_por_id(cliente_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, apellido, telefono, mail, nota FROM Clientes WHERE id = ?", cliente_id)
    row = cursor.fetchone() # Usamos fetchone() para obtener una sola fila
    cursor.close()
    conn.close()
    return row

# 🟢 Actualizar un cliente
def actualizar_cliente_db(cliente_id: int, cliente_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Asegúrate de que las columnas coincidan con las de tu tabla Clientes
    cursor.execute(
        "UPDATE Clientes SET nombre = ?, apellido = ?, telefono = ?, mail = ?, nota = ? WHERE id = ?",
        (cliente_data.nombre, cliente_data.apellido, cliente_data.telefono, cliente_data.mail, cliente_data.nota, cliente_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Cliente actualizado con éxito"}

# 🟢 Eliminar un cliente por su ID
def eliminar_cliente_db(cliente_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", cliente_id)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Cliente eliminado con éxito"} # O simplemente un booleano de éxito