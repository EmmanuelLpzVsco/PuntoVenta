# Punto de Venta

Este repositorio contiene un API para punto de venta el cual corre como un servicio dentro de un contenedor Docker.

## 1. Instalación

Construir la imagen `puntodevent` con base en la definición del `Dockerfile`:

```
$ docker build -t puntodeventa .
```

## 2. Levantar el servicio

Correr la imagen `puntodeventa`

```
$ docker run -p 8080:8080 puntodeventa
```

El servicio será accesible a través en `http://localhost:8080`

## Endpoints:

## 1. Recuperar todos los productos
Método: GET
URL: /productos
Respuesta: Un objeto JSON que contiene una lista de todos los productos de la tabla "productos".

## 2. Recuperar un producto específico por ID
Método: GET
URL: /productos/<id> Respuesta: Un objeto JSON que contiene los detalles del producto con el ID dado.

## 3. Agregar un nuevo producto
Método: POST
URL: /productos
Solicitud: un objeto JSON que contiene los detalles del nuevo producto, incluidos "nombre" (string), "precio" (float) y "cantidad" (entero).
Respuesta: un objeto JSON que contiene el ID, el nombre, el precio y la cantidad del producto recién agregado.

## 4. Actualizar un producto existente
Método: PUT
URL: /productos/<id> Solicitud: Un objeto JSON que contiene los detalles del producto que se va a actualizar, incluidos "nombre" (string), "precio" (float) y "cantidad" (entero).
Respuesta: Un objeto JSON que contiene los detalles actualizados del producto con el ID dado.

## 5. Eliminar un producto
Método: GET
URL: /eliminar_producto/<id> Respuesta: Elimina el producto con el ID dado de la tabla "productos" y redirige al usuario a la lista de todos los productos.

Nota: La API se compila utilizando el marco Bottle y se ejecuta en modo de depuración. El archivo de base de datos SQLite "ventas.db" debe estar presente en el mismo directorio que el script.