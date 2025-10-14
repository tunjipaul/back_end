from http.server import BaseHTTPRequestHandler, HTTPServer

import json

data = [
    {"id": 1, "name": "Paul"},
    {"id": 2, "name": "Jane"}
]
#class for simple API server using put method.

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PUT(self):
            content_size = int(self.headers.get('Content-Length', 0))
            parsed_data = self.rfile.read(content_size)
            update_data = json.loads(parsed_data)
            
            for index, item in enumerate(data):
                if item['id'] == update_data['id']:
                    data[index] = update_data
                    self.send_data({
                        "message": "data updated",
                        "data": update_data
                    })
                    return
            self.send_data({
                "message": "data not found"
            }, status = 404)

def run():
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()
print("Application is running ")
run()

