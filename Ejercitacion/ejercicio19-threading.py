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

    addr_info = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)

    for addr in addr_info:
        family, socktype, proto, canonname, sockaddr = addr
        server_socket = socket.socket(family, socktype, proto)
        server_socket.bind(sockaddr)
        server_socket.listen(7)


    while True:
        client_socket, client_address = server_socket.accept()
        
        client_thread = th.Thread(target=managment_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

