""" EJERCICIOS 
1 - Cuándo y por qué se produce el error BrokenPipeError: [Errno 32] Broken pipe ?

--> Cuando el extremo receptor de un socke/tubería ya no está disponible para recibir más datos. Porque una de las partes cierra el flujo de datos antes de que la otra parte haya terminado de enviar todos los datos.

2 - Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes de forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.

El hilo/proceso hijo debe responder con mayúsculas hasta que el cliente envíe la palabra exit. 

En caso de exit el cliente debe administrar correctamente el cierre de la conexión y del proceso/hilo."""

import socket
import threading as th


def managment_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if data.strip().lower() == b'exit' or data == b'':
            break
        answer = data.upper()
        client_socket.send(answer)
    client_socket.close()

def main():
    host = "127.0.0.1"  
    port = 30501 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(7)


    while True:
        client_socket, client_address = server_socket.accept()
        
        client_thread = th.Thread(target=managment_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

