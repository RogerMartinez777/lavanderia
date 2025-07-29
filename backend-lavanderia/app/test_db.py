# test_db.py
import sys
import os

print("DEBUG: Script test_db.py iniciado.") # DEBUG PRINT

# 🟢 CAMBIO AQUÍ: Si test_db.py está dentro de la carpeta 'app/'
# y db.py también está dentro de 'app/', entonces db.py es un módulo hermano.
# La importación debe ser relativa.
# La línea sys.path.insert anterior ya no es necesaria aquí.
try:
    from . import db
    print("DEBUG: Módulo db importado correctamente.") # DEBUG PRINT
except ImportError as e:
    print(f"ERROR: Fallo al importar db.py: {e}") # DEBUG PRINT
    sys.exit(1) # Salir si la importación falla

try:
    print("DEBUG: Intentando abrir conexión a la base de datos y ejecutar inserción.") # DEBUG PRINT
    new_id = db.insertar_categoria_servicio("PruebaID")
    print(f"ID insertado (desde db.py): {new_id}, Tipo: {type(new_id)}")
except RuntimeError as e:
    print(f"RuntimeError capturado: {e}")
except Exception as e:
    print(f"Otro error capturado: {e}")
finally:
    print("DEBUG: Bloque finally de test_db.py.") # DEBUG PRINT
    # Opcional: limpiar la categoría de prueba si se insertó
    # Asegúrate de que new_id se haya definido antes de intentar eliminar
    if 'new_id' in locals() and new_id is not None:
        try:
            print(f"DEBUG: Intentando eliminar categoría de prueba con ID {new_id}...") # DEBUG PRINT
            # Asegúrate de que la función eliminar_categoria_servicio exista y funcione
            if db.eliminar_categoria_servicio(int(new_id)):
                print("Categoría de prueba eliminada con éxito.")
            else:
                print("No se pudo eliminar la categoría de prueba (quizás ya no existía).")
        except Exception as e:
            print(f"Error al intentar eliminar categoría de prueba: {e}")
    print("DEBUG: Script test_db.py finalizado.") # DEBUG PRINT