FROM python:3.12-alpine

# 1. ACTUALIZACIÓN Y HERRAMIENTAS (OS Level)
# Agregamos 'curl' aquí porque 'apk' requiere permisos de root.
# Lo hacemos antes de crear al usuario limitado.
RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache curl

WORKDIR /app

# 2. ACTUALIZACIÓN DE PIP
RUN pip install --no-cache-dir --upgrade pip

# dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# código
COPY app.py .

# 3. SEGURIDAD DE EJECUCIÓN (User Level)
# Creamos el usuario y cambiamos a él al final del proceso.
RUN adduser -D samuel-user
USER samuel-user

EXPOSE 8000

# El Health Check de Docker Compose usará el 'curl' que instalamos arriba
CMD ["python", "app.py"]
