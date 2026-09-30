import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DATA_DIR = "/data"
STATE_FILE = os.path.join(DATA_DIR, "state.json")
PORT = 8080


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(STATE_FILE):
        state = {
            "site": "Kithive",
            "initialized_at": datetime.now(timezone.utc).isoformat(),
            "status": "ready",
        }
        with open(STATE_FILE, "w", encoding="utf-8") as handle:
            json.dump(state, handle, indent=2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ensure_data_dir()

        if self.path in {"/", "/health", "/healthz"}:
            payload = {
                "name": "Kithive",
                "status": "ok",
                "data_dir": DATA_DIR,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            body = json.dumps(payload, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    ensure_data_dir()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving Kithive on port {PORT}")
    server.serve_forever()
