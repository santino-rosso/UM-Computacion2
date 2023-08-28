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

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(7)


    while True:
        client_socket, client_address = server_socket.accept()
        
        client_process = mp.Process(target=managment_client, args=(client_socket,))
        client_process.start()
        client_socket.close()

if __name__ == "__main__":
    main()

