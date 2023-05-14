"""
Memoria Compartida

Etapa 1
Escribir un programa que reciba por argumento la opción -f acompañada de un path_file

El programa deberá crear un segmento de memoria compartida y generar dos hijos H1 y H2.

H1 deberá leer desde sdtin lo que ingrese el usuario, línea por línea, enviando una señal USR1 al padre en cada línea leida.

Una vez ingresada una línea, el proceso padre leerá la memoria compartida y mostrará la línea leida por pantalla y enviará una señal USR1 a H2.

Al recibir la señal USR1, H2 leerá la línea desde la memoria compartida y la escribirá en mayúsculas en el archivo recibido como argumento.

Etapa 2
Cuando el usuario introduzca "bye" en la terminal, H1 enviará al padre la señal USR2 y terminará.

Al recibir la señal USR2, el padre, la enviará a H2 que también terminará.

El padre esperará a ambos hijos y terminará también.
"""

import argparse
import mmap
import os
import signal


if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-f', type=str, help='Ruta del archivo.')
    args = argparser.parse_args()

    if os.path.exists(args.f):
        os.remove(args.f)

    memoria = mmap.mmap(-1, 20)

    def señal_padre(signum, frame):
        if signum == signal.SIGUSR1:
            memoria.seek(0)
            linea = memoria.read(20)
            print(linea.decode())
            os.kill(H2, signal.SIGUSR1)
        elif signum == signal.SIGUSR2:
            os.kill(H2, signal.SIGUSR2)
            os.waitpid(H1, 0)
            os.waitpid(H2, 0)
            os._exit(0)

    def señal_H2(signum, frame):
        if signum == signal.SIGUSR1:
            memoria.seek(0)
            linea = memoria.read(20).decode()
            with open(args.f, 'a') as archivo:
                archivo.write(linea.upper())
            os.kill(H1, signal.SIGUSR1)
        elif signum == signal.SIGUSR2:
            os._exit(0)
        
    def señal_H1(signum, frame):
        if signum == signal.SIGUSR1:
            pass
        

    signal.signal(signal.SIGUSR1, señal_padre)
    signal.signal(signal.SIGUSR2, señal_padre)

    
    H1 = os.fork()    
    if H1 == 0:
        while True:
            signal.signal(signal.SIGUSR1, señal_H1)
            linea = input("Ingresar linea: ")
            linea = linea.rstrip() 
            if linea == 'bye':
                os.kill(os.getppid(), signal.SIGUSR2)
                os._exit(0)
            else:
                memoria.seek(0)
                memoria.write(linea.encode())
                os.kill(os.getppid(), signal.SIGUSR1)
                signal.pause()
    else:
        H2 = os.fork()
        if H2 == 0:
            signal.signal(signal.SIGUSR1, señal_H2)
            signal.signal(signal.SIGUSR2, señal_H2)
            while True:
                signal.pause()
        else:
            while True:
                signal.pause()
            