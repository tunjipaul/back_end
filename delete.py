from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {"id": 1, "name": "Paul"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "John"}
]

#delete method to delete data from the list.
class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_DELETE(self):
            content_size = int(self.headers.get('Content-Length', 0))
            parsed_data = self.rfile.read(content_size)
            delete_data = json.loads(parsed_data)
            
            for index, item in enumerate(data):
                if item['id'] == delete_data['id']:
                    deleted_item = data.pop(index)
                    self.send_data({
                        "message": "data deleted",
                        "data": deleted_item
                    })
                    return
            self.send_data({
                "message": "data not found"
            }, status = 404)

def run():
    HTTPServer(('localhost', 7000), BasicAPI).serve_forever()
print("Application is running ")
run()

