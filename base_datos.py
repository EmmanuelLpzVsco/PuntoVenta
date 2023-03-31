"""
Base de datos
"""

import sqlite3
from sqlite3 import Error

def crear_conexion():
    # Creamos una conexión a la base de datos
    try:
        conexion = sqlite3.connect('ventas.db')
        return conexion
    except Error as e:
        print(e)
        return None

def crear_tabla_productos():
    # Creamos la tabla "productos" en la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                    (id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    cantidad INTEGER NOT NULL)''')
    conexion.commit()
    cerrar_conexion(conexion)

def cerrar_conexion(conexion):
    # Cerramos la conexión a la base de datos
    conexion.close()

def obtener_productos():
    # Obtenemos todos los productos de la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    cerrar_conexion(conexion)
    return productos

def obtener_producto(id_producto):
    # Obtenemos un producto en particular de la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id_producto = ?', (id_producto,))
    producto = cursor.fetchone()
    cerrar_conexion(conexion)
    return producto

def agregar_producto(nombre, precio, cantidad):
    # Agregamos un nuevo producto a la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO productos(nombre, precio, cantidad) VALUES(?,?,?)', (nombre, precio, cantidad))
    conexion.commit()
    id_producto = cursor.lastrowid
    cerrar_conexion(conexion)
    return id_producto

def actualizar_producto(id_producto, nombre=None, precio=None, cantidad=None):
    # Actualizamos un producto existente en la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    campos = []
    valores = []
    if nombre:
        campos.append('nombre = ?')
        valores.append(nombre)
    if precio:
        campos.append('precio = ?')
        valores.append(precio)
    if cantidad:
        campos.append('cantidad = ?')
        valores.append(cantidad)
    
    campos_str = ', '.join(campos)
    valores.append(id_producto)
    consulta = f'UPDATE productos SET {campos_str} WHERE id_producto = ?'
    cursor.execute(consulta, tuple(valores))
    conexion.commit()
    cerrar_conexion(conexion)

def eliminar_producto(id_producto):
    # Eliminamos un producto de la base de datos
    conexion = crear_conexion()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM productos WHERE id_producto = ?', (id_producto,))
    conexion.commit()
    cerrar_conexion(conexion)
