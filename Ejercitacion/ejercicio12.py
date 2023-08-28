"""
1 - Escribir un programa que reciba un mensaje desde otro proceso usando fifo (pipes con nombre). 
El proceso receptor deberá lanzar tantos hilos como líneas tenga el mensaje y deberá enviar cada línea a los hilos secundarios. 
Cada hilo secundario deberá calcular la cantidad de caracteres de su línea y COMPROBAR la cuenta de la línea anterior."""

import multiprocessing, os, threading

def funcion_del_hilo(linea):
    numero_de_caracteres = len(linea)
    print(f"La linea {linea} tiene {numero_de_caracteres} caracteres")
    evento.set()

def leer_consola():
    mensaje = "hola\ncomo\nestas\n"
    with open(fifo_1, "w") as fifo:
        fifo.write(mensaje)
    
def receptor():
    x = 0
    with open(fifo_1, "r") as fifo:
        lineas = fifo.readlines()
        lineas = [linea.strip() for linea in lineas]
        for linea in lineas:
            if x != 0:
                evento.wait()
            hilo = threading.Thread(target=funcion_del_hilo, args=(linea,))
            hilo.start()
            x += 1



if __name__ == '__main__':

    fifo_1 = "mi_fifo"

    if os.path.exists(fifo_1):
        os.remove(fifo_1)

    os.mkfifo(fifo_1)

    evento = threading.Event()


    proceso_1 = multiprocessing.Process(target=leer_consola)
    proceso_2 = multiprocessing.Process(target=receptor)

    proceso_1.start()
    proceso_2.start()
