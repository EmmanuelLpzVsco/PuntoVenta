# Imagen base
FROM python:3.8-slim-buster

# Agregamos dependencias SQLite3
RUN apt-get update && \
    apt-get install -y sqlite3 libsqlite3-dev

# Creamos el directorio de trabajo y movemos el código de la aplicación
WORKDIR /app

# Copiamos el código de la aplicación al contenedor
COPY . /app


# Instalamos las dependencias Python necesarias
RUN pip install bottle requests

# Exponemos el puerto 8080 (puerto que usa Bottle por defecto)
EXPOSE 8080

# Ejecutamos la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]