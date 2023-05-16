"""Considerando el programa noblock.py, realizar un programa que lance dos procesos hijos que intenten encontrar el nonce para un No-Bloque con una dificultad dada. 
El hijo que lo encuentre primero debe comunicarse con el padre mediante una señal guardando el nonce en una fifo para que el padre pueda leerla. 
Hacer otra versión pero utilizando pipes."""

import os
import signal
from noblock import NoBlock, proof_of_work


def leer_nonce(signum, frame):
    if signum == signal.SIGUSR1:
        nonce = os.read(l_padre, 1024)
        print(nonce.decode('utf-8'))
        os._exit(0)

def Proceso_hijo(block,e):
    hash, nonce = proof_of_work(block)
    nonce = str(nonce)
    os.write(e, nonce.encode('utf-8'))
    os.kill(os.getppid(), signal.SIGUSR1)
    os._exit(0)



if __name__ == '__main__':

    signal.signal(signal.SIGUSR1, leer_nonce)

    l_padre, e_hijo = os.pipe()
    b = NoBlock(seed='La semilla que quiera', nonce=0)
    h1 = os.fork()
    if h1 == 0:
        Proceso_hijo(b,e_hijo)
    else:
        h2 = os.fork()
        if h2 == 0:
            Proceso_hijo(b,e_hijo)
        else:
            os.wait()
    
