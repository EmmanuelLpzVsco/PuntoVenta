# PuntoVenta

ejecuta el siguiente comando desde ese directorio:

docker build -t puntodeventa .

Esto creará una imagen llamada puntodeventa que puede ser ejecutada
en otro computador. Para ejecutar la imagen, usa el siguiente comando:

docker run -p 8080:8080 puntodeventa

Esto iniciará un contenedor a partir de la imagen puntodeventa y 
redirigirá el puerto 8080 del contenedor al puerto 8080 de la máquina host. 
La aplicación PuntodeVenta.pyestará disponible en http://localhost:8080.

Endpoints:

Recuperar todos los productos
Método: GET
URL: /productos
Respuesta: Un objeto JSON que contiene una lista de todos los productos de la tabla "productos".

Recuperar un producto específico por ID
Método: GET
URL: /productos/<id> Respuesta: Un objeto JSON que contiene los detalles del producto con el ID dado.

Agregar un nuevo producto
Método: POST
URL: /productos
Solicitud: un objeto JSON que contiene los detalles del nuevo producto, incluidos "nombre" (string), "precio" (float) y "cantidad" (entero).
Respuesta: un objeto JSON que contiene el ID, el nombre, el precio y la cantidad del producto recién agregado.

Actualizar un producto existente
Método: PUT
URL: /productos/<id> Solicitud: Un objeto JSON que contiene los detalles del producto que se va a actualizar, incluidos "nombre" (string), "precio" (float) y "cantidad" (entero).
Respuesta: Un objeto JSON que contiene los detalles actualizados del producto con el ID dado.

Eliminar un producto
Método: GET
URL: /eliminar_producto/<id> Respuesta: Elimina el producto con el ID dado de la tabla "productos" y redirige al usuario a la lista de todos los productos.

Nota: La API se compila utilizando el marco Bottle y se ejecuta en modo de depuración. El archivo de base de datos SQLite "ventas.db" debe estar presente en el mismo directorio que el script.