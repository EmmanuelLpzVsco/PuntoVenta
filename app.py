"""
Punto de venta
"""

import requests
import json
import sqlite3
from bottle import Bottle, request, response, HTTPResponse

app = Bottle(__name__)

# Definimos la ruta para obtener todos los productos
@app.get('/productos')
def obtener_productos()-> dict[str, list]:
    # Creamos una conexión a la base de datos
    conexion = sqlite3.connect('ventas.db')

    # Leemos todos los datos de la tabla "productos"
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    # Cerramos la conexión a la base de datos
    conexion.close()

    # Retornamos los datos en formato JSON
    return {'productos': productos}

# Definimos la ruta para obtener un producto en particular
@app.get('/productos/<id>')
def obtener_producto(id)-> (HTTPResponse | dict[str, list]):
    # Creamos una conexión a la base de datos
    conexion = sqlite3.connect('ventas.db')

    # Leemos el producto con el id solicitado
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id_producto = ?', (id,))
    producto = cursor.fetchone()

    # Cerramos la conexión a la base de datos
    conexion.close()

    # Si el producto no existe, retornamos el 404
    if producto is None:
        return HTTPResponse(status=404)
        
    #Retornamos el producto en formato JSON    
    return {'producto': producto}


# Definimos la ruta para agregar un nuevo producto
@app.post('/productos')
def agregar_producto():
    # Obtenemos los datos del producto desde la solicitud
    nombre = request.json.get('nombre')
    precio = request.json.get('precio')
    cantidad = request.json.get('cantidad')

    #Validamos que los datos estén completos
    if not nombre or not precio or not cantidad:
        return HTTPResponse(status=400)

    # Creamos una conexión a la base de datos
    conexion = sqlite3.connect('ventas.db')

    # Insertamos el nuevo producto en la tabla
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO productos(nombre, precio, cantidad) VALUES(?,?,?)', (nombre, precio, cantidad))
    conexion.commit()

    # Obtenemos el id del nuevo producto
    id_producto = cursor.lastrowid

    # Cerramos la conexión a la base de datos
    conexion.close()

    # Retornamos los datos del nuevo producto en formato JSON
    response.status = 201
    return {'id_producto': id_producto, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

# Definimos la ruta para actualizar un producto existente
@app.put('/productos/<id>')
def actualizar_producto(id):
    # Obtenemos los datos del producto desde la solicitud
    nombre = request.json.get('nombre')
    precio = request.json.get('precio')
    cantidad = request.json.get('cantidad')

    #Validamos que al menos uno de los campos a actualizar este presente
    if not nombre and not precio and not cantidad:
        return HTTPResponse(status=400)

    # Creamos una conexión a la base de datos
    conexion = sqlite3.connect('ventas.db')

    # Actualizamos el producto con el ID especificado
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
    valores.append(id)
    consulta = f'UPDATE productos SET {campos_str} WHERE id_producto = ?'
    cursor.execute(consulta, tuple(valores))
    conexion.commit()

    # Cerramos la conexión a la base de datos
    conexion.close()

    # Retornamos los datos del producto actualizado en formato JSON
    return obtener_producto(id)


#Eliminar producto
@app.get('eliminar_producto/<id>')
def eliminar_producto(id):
    #Creamos la conexion a base de datos
    conexion = sqlite3.connect('ventas.db')

    #Eliminamos el producto de la tabla "productos"
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM productos WHERE id_producto = ?', (id,))
    conexion.commit()

    # Cerramos la conexion a la base de datos
    conexion.close()

    #Redireccionamos al usuario a la lista de productos
    return HTTPResponse(status=303, headers={'Location': '/productos'})


#Iniciar la aplicacion
if __name__=='__main__':
    app.run(debug=True)   