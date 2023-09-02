"""## EJERCICIOS ##
1 - Realizar un programa que implemente un servidor TCP o UDP usando socketserver.
El servidor puede ser un servidor de mayúsculas, un codificador en rot13 o cualquier otra tarea simple.
Se debe implementar concurrencia usando forking o threading."""

import socketserver
import threading


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if data == b'':
                break
            response = data.upper()+"\n".encode()
            self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
 
 
def exit_handler():
    print("Exiting...")
    server.shutdown()

 
if __name__ == "__main__":

    host, port = "0.0.0.0", 30051

    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)

    with server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        
        input("Press any key to exit...\n")
        exit_handler()

