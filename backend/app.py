from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import start_http_server, Counter
import json
import os
import redis

# 1. Configuración de Métricas (Fuera de la clase)
REQUESTS = Counter('backend_visitas_total', 'Total de visitas al búnker')

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 2. Incrementamos la métrica en cada visita
        REQUESTS.inc()

        try:
            visitas = db.incr("contador_visitas")
        except Exception:
            visitas = "redis_no_disponible"

        data = {
            "mensaje": "Backend Python con Métricas Activo",
            "visitas": visitas
        }

        body = json.dumps(data).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return

def main():
    # 3. Iniciamos el servidor de métricas en un hilo aparte (puerto 8001)
    start_http_server(8001)
    
    port = 8000
    print(f"App en puerto {port} | Métricas en puerto 8001")
    HTTPServer(("", port), Handler).serve_forever()

if __name__ == "__main__":
    main()
# Automatización completada con éxito
