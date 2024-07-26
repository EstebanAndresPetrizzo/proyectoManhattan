# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido del directorio actual en el contenedor
COPY . .

# Expone el puerto en el que la app Flask estará corriendo
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]