from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        body = self.rfile.read(length)
        data = json.loads(body)

        print("\n" + "="*50)
        print(f"ALERTES REÇUES : {len(data.get('alerts', []))}")
        for alert in data.get('alerts', []):
            status = alert.get('status', '?').upper()
            name   = alert['labels'].get('alertname', '?')
            summary = alert['annotations'].get('summary', '?')
            print(f"  [{status}] {name} — {summary}")
        print("="*50 + "\n")

        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass   # Supprime les logs HTTP parasites

print("Webhook logger démarré sur le port 5001...")
HTTPServer(('0.0.0.0', 5001), WebhookHandler).serve_forever()
