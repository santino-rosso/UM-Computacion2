"""
1 - Escribir un programa que genere dos hilos utilizando threading.
Uno de los hilos debera leer desde stdin el texto ingresado por el usuario y deberá escribirlo en una cola de mensajes (queue).
El segundo hilo deberá leer desde la queue el contenido y encriptará dicho texto utilizando el algoritmo ROT13 y lo almacenará en una cola de mensajes (queue).
El primer hilo deberá leer dicho mensaje de la cola y lo mostrará por pantalla.
ROT13
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
gato (claro)->(rot13) tngb"""

import threading, queue, sys, codecs

cola_encripada = queue.Queue()
cola = queue.Queue()

def leer():
    while True:
        print("Ingrese una linea de texto para codificar en ROT13('salir' para terminar el programa): ")
        linea = sys.stdin.readline().strip()
        if linea == "salir":
            break
        cola.put(linea)
        linea_termianda = cola_encripada.get()
        print(linea_termianda)
        print("")

def encriptar():
    while True:
        linea_encriptar = cola.get()
        linea_encriptada = codecs.encode(linea_encriptar, "rot_13")
        cola_encripada.put(linea_encriptada)



if __name__ == "__main__":
    th_lectura = threading.Thread(target=leer, daemon=False)
    th_lectura.start()
    th_encritador = threading.Thread(target=encriptar, daemon=True)
    th_encritador.start()

