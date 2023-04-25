"""Escribir un programa que realice la multiplicación de dos matrices de 2x2. 
Cada elemento deberá calcularse en un proceso distinto devolviendo el resultado en una fifo indicando el indice del elemento. 
El padre deberá leer en la fifo y mostrar el resultado final."""

import os


matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]


fifo = '/tmp/fifo1.txt'


def calcular_elemento(i):
    fila = i // 2
    columna = i % 2
    
    resultado = 0
    for j in range(2):
        resultado += matriz_a[fila][j] * matriz_b[j][columna]
            
    with open('/tmp/fifo1.txt', 'a') as fifo:
        fifo.write(f'{fila},{columna},{resultado}\n')
    os._exit(0)
    

def crear_procesos():
    for i in range(4):
        if os.fork() == 0:
            calcular_elemento(i)      
    proceso_padre()

def proceso_padre():
    matriz_r = [[None,None],[None,None]]
    with open('/tmp/fifo1.txt', 'r') as fifo:
        for linea in fifo:
            fila, columna, resultados = linea.split(',')
            matriz_r[int(fila)][int(columna)] = int(resultados.strip())
    print(matriz_r)

    os.unlink('/tmp/fifo1.txt')


# inicio del codigo

if __name__ == '__main__':

    if not os.path.exists(fifo):
        os.mkfifo(fifo)
         
    crear_procesos()

