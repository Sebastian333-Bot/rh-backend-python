# 1. Imagen base oficial y ligera de Python
FROM python:3.11-slim

# 2. Carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar la lista de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código del backend
COPY . .

# 5. Puerto en el que corre tu app Flask
EXPOSE 8080

# 6. Comando para iniciar la aplicación
CMD ["python", "app.py"]