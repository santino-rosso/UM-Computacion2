"""Considerando el programa noblock.py, realizar un programa que lance dos procesos hijos que intenten encontrar el nonce para un No-Bloque con una dificultad dada. 
El hijo que lo encuentre primero debe comunicarse con el padre mediante una señal guardando el nonce en una fifo para que el padre pueda leerla. 
Hacer otra versión pero utilizando pipes."""

import os
import signal
from noblock import NoBlock, proof_of_work


def leer_nonce(signum, frame):
    if signum == signal.SIGUSR1:
        with open(fifo, 'r') as f:
            nonce = f.read()
            print(nonce)
        os.remove(fifo)
        os._exit(0)
        
def Proceso_hijo(block):
    hash, nonce = proof_of_work(block)
    os.kill(os.getppid(), signal.SIGUSR1)
    with open(fifo, 'w') as f:
        f.write(str(nonce))
    os._exit(0)


if __name__ == '__main__':

    fifo = '/tmp/fifo.txt'

    if not os.path.exists(fifo):
        os.mkfifo(fifo)

    signal.signal(signal.SIGUSR1, leer_nonce)

    b = NoBlock(seed='La semilla que quiera', nonce=0)
    h1 = os.fork()
    if h1 == 0:
        Proceso_hijo(b)
    else:
        h2 = os.fork()
        if h2 == 0:
            Proceso_hijo(b)
        else:
            os.wait()
