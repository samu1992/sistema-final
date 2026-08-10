# ==========================================
# Etapa 1: Constructor (Builder)
# ==========================================
FROM python:3.12-alpine AS builder

WORKDIR /app

# Actualizamos pip y preparamos dependencias
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .

# Instalamos las librerías en un entorno de usuario (--user)
RUN pip install --user --no-cache-dir -r requirements.txt

# ==========================================
# Etapa 2: Producción (Runner)
# ==========================================
FROM python:3.12-alpine AS runner

# 1. ACTUALIZACIÓN Y HERRAMIENTAS (Como lo tenías vos)
RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache curl

WORKDIR /app

# 2. SEGURIDAD DE EJECUCIÓN (Tu usuario)
RUN adduser -D samuel-user

# 3. MUDANZA MULTI-STAGE
# Traemos LAS LIBRERÍAS ya instaladas desde la Etapa 1
COPY --from=builder /root/.local /home/samuel-user/.local
# Traemos EL CÓDIGO de tu bot
COPY app.py .

# Ajustamos los permisos para tu usuario
RUN chown -R samuel-user:samuel-user /app

# Seteamos variables para que Python encuentre las librerías del builder
ENV PATH=/home/samuel-user/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

USER samuel-user

EXPOSE 8000

CMD ["python", "app.py"]
