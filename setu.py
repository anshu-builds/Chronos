import socket
import json
import os

from lib import base

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8081))
    server_socket.listen(5)
    print("🌉 Setu API is waiting on http://127.0.0.1:8081...")

    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024).decode('utf-8')

        if not request:
            client_socket.close()
            continue

        try:
            path = request.split(' ')[1]
        except IndexError:
            path = '/'

        if path == '/log': 
            if os.path.exists(".chronos/objects"):
                files = os.listdir(".chronos/objects")
                data = {"type":"Raw Inventory","count": len(files), "objects": files}
            else:
                data ={"Error": "No Database Found"}
        else:
            if os.path.exists(".chronos"):
                files = os.listdir(".chronos/objects")
                data ={"system":"Chronos VCS", "status":"Online", "total_objects": len(files)}
            else:
                data ={"Error": "Chronos not initialized"}

        json_response =json.dumps(data)
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
            f"{json_response}"
        )
        
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
    