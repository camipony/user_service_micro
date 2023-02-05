# Usamos una imagen de Python como base
FROM python:3.9

# Establecemos la carpeta de trabajo
WORKDIR /app

# Copiamos los archivos de la aplicación a la carpeta de trabajo
COPY . .

# Instalamos las dependencias
RUN pip install -r requirements.txt

# Exponemos el puerto 8000 para que la aplicación pueda recibir solicitudes
EXPOSE 8000

# Ejecutamos la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
