# PuntoVenta

ejecuta el siguiente comando desde ese directorio:

docker build -t puntodeventa .

Esto creará una imagen llamada puntodeventa que puede ser ejecutada
en otro computador. Para ejecutar la imagen, usa el siguiente comando:

docker run -p 8080:8080 puntodeventa

Esto iniciará un contenedor a partir de la imagen puntodeventa y 
redirigirá el puerto 8080 del contenedor al puerto 8080 de la máquina host. 
La aplicación PuntodeVenta.pyestará disponible en http://localhost:8080.