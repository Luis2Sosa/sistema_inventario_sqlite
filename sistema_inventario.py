import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("inventario.db")
    conexion.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    );
    """)
    conexion.close()

def agregar_producto():
    nombre = input("Ingrese el nombre del producto:\n").lower().strip()
    precio = int(input("Ingrese el precio del producto:\n"))
    conexion = sqlite3.connect("inventario.db")
    conexion.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?);", (nombre, precio))
    conexion.commit()
    conexion.close()
    print("Producto agregado correctamente.")

def ver_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.execute("SELECT * FROM productos;")
    print("---Productos del inventario---\n")
    for fila in cursor:
        print(f"ID: {fila[0]} | Nombre: {fila[1]} | Precio: {fila[2]}")
    conexion.close()
    
def modificar_producto():
    id_buscar = int(input("ID del producto a buscar:\n"))
    nuevo_nombre = input("Ingrese el nuevo nombre del producto (dejar en blanco para no cambiar):\n").lower().strip()
    nuevo_precio_input = input("Ingrese el nuevo precio del producto (dejar en blanco para no cambiar):\n").strip()
    
    conexion = sqlite3.connect("inventario.db")
    if nuevo_nombre:
        conexion.execute("UPDATE productos SET nombre = ? WHERE id = ?;", (nuevo_nombre, id_buscar))
    
    if nuevo_precio_input:
        nuevo_precio = float(nuevo_precio_input)
        conexion.execute("UPDATE productos SET precio = ? WHERE id = ?;", (nuevo_precio, id_buscar))
    
    conexion.commit()
    conexion.close()
    print("Producto actualizado correctamente.")
    
def eliminar_productos():
    id_buscar = int(input("ID del producto a eliminar:\n"))
    conf = input(f"Estas seguro de querer eliminar {id_buscar}? del inventario? (si/no):\n").lower().strip()
    
    if conf == "si":
        conexion = sqlite3.connect("inventario.db")
        conexion.execute("DELETE FROM productos WHERE id = ?;", (id_buscar,))
        conexion.commit()
        conexion.close()
        print("Producto eliminado correctamente.")
    else:
        print("Eliminación cancelada.")
        
def menu():
    crear_tabla()
    
    while True:
        print("--- SISTEMA DE INVENTARIO ---\n")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar Producto")
        print("4. Eliminar producto")
        print("5. Salir\n")
        
        opcion = input("Ingrese un numero de opción:\n").strip()
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_productos()
        elif opcion == "5":
            print("Gracias por Utilizar el Sistema de Inventario.")
            break
        else:
            print("Opción no valida.")
            
if __name__ == "__main__":
    menu()