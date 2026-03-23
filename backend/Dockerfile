FROM python:3.12-alpine

# 1. ACTUALIZACIÓN DE SEGURIDAD (OS Level)
# Esto limpia el error de zlib y otras librerías del sistema
RUN apk update && apk upgrade --no-cache

WORKDIR /app

# 2. ACTUALIZACIÓN DE PIP (Herramientas Level)
# Esto limpia las vulnerabilidades propias de pip que marcó Trivy
RUN pip install --no-cache-dir --upgrade pip

# dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# código
COPY app.py .

# 3. SEGURIDAD DE EJECUCIÓN (User Level)
# Por defecto Docker corre como 'root'. En DevOps, eso es pecado.
# Creamos un usuario sin privilegios para que, si hackean la app, no tengan control del sistema.
RUN adduser -D samuel-user
USER samuel-user

EXPOSE 8000

CMD ["python", "app.py"]
