"""## EJERCICIOS ##
En el ejercicio de la clase 15 se proponía el siguiente ejercicio:

**Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes de forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.**

1- Actualizar el servidor para que funcione indistintamente con IPv4 e IPv6"""

import socket, signal
import multiprocessing as mp

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

def managment_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if data.strip().lower() == b'exit' or data == b'':
            break
        answer = data.upper()
        client_socket.send(answer)
        

def main():
    host = "127.0.0.1"  
    port = 30501

    addr_info = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    
    for addr in addr_info:
        family, socktype, proto, canonname, sockaddr = addr
        server_socket = socket.socket(family, socktype, proto)
        server_socket.bind(sockaddr)
        server_socket.listen(7)


    while True:
        client_socket, client_address = server_socket.accept()
        
        client_process = mp.Process(target=managment_client, args=(client_socket,))
        client_process.start()
        client_socket.close()

if __name__ == "__main__":
    main()

