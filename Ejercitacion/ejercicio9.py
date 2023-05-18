"""
Considerando el programa noblock.py, realizar un programa que lance 10 procesos hijos que intenten encontrar el nonce para un No-Bloque con una dificultad dada. 
El hijo que lo encuentre primero debe comunicarse con el padre. Realizar todo utilizando multiprocessing
"""

from multiprocessing import Pipe, Process
from Ejercicio7.noblock import NoBlock, proof_of_work


def Proceso_hijo(block, conexión_h):
    hash, nonce = proof_of_work(block)
    nonce = str(nonce)
    conexión_h.send(nonce)
    conexión_h.close()



if __name__ == '__main__':

    b = NoBlock(seed='La semilla que quiera', nonce=0)
   
    conexión_p, conexión_h = Pipe()
    for x in range(10):
        h = Process(target=Proceso_hijo, args=(b,conexión_h))
        h.start()
    nonce = conexión_p.recv()
    print(nonce)
