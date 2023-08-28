"""
Escribir un programa que implemente un socket pasivo que gestione de forma serializada distintas conecciones entrantes.

Debe atender nuevas conexiones de forma indefinida.

NOTA: cuando decimos serializado decimo que atiende una conexión y recibe una nueva conección una vez que esa conexión se cerró
"""

import socket


def managment_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if data == b'':
            break  
        print("Recibido:", data)  
    
    print("Cerrando conexión con:", client_address)
    client_socket.close()

def main():
    host = "127.0.0.1"  
    port = 30500        

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  

    print("Esperando conexión en: ", host, ":", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexión entrante de:", client_address)
        managment_client(client_socket, client_address)

if __name__ == "__main__":
    main()
