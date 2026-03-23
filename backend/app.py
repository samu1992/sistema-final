from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import redis


# Service Discovery: el host viene del compose (nombre del servicio redis)
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Contador persistente en Redis
        try:
            visitas = db.incr("contador_visitas")  # INCR crea si no existe
        except Exception as e:
            # si Redis no está disponible, respondemos igual
            visitas = None

        data = {
            "mensaje": "Backend Python activo (detrás de Nginx)",
            "ruta": self.path,
            "visitas": visitas if visitas is not None else "redis_no_disponible"
        }

        body = json.dumps(data).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def main():
    host = ""   # 0.0.0.0 (clave para Docker)
    port = 8000
    print(f"Backend escuchando en 0.0.0.0:{port} (Redis: {REDIS_HOST}:{REDIS_PORT})")
    HTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
