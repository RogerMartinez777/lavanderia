// para cargar el backend, se entra asi por la ubicacion del main.py:

uvicorn app.main:app --reload

// para servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

---FLUJO EN ORDEN:
El usuario abre ClientesView.vue ➡️ se ejecuta una función que hace un fetch a /clientes.

FastAPI (main.py) recibe la petición y la redirige al archivo clientes.py.

clientes.py llama a get_db_connection() desde db.py, y ejecuta un SELECT SQL sobre la tabla Clientes.

Se transforman los resultados SQL a JSON (lista de diccionarios).

FastAPI responde al frontend con los datos.

Vue renderiza los datos y los muestra en pantalla.
