"""Escribir un programa en Python que comunique dos procesos. 
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número."""

import subprocess
import argparse
import sys


def Comunicador_Procesos():

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', type=str, help='Nombre del archivo del proceso hijo.')
    argparser.add_argument('-t', type=str, help='Nombre del archivo de texto a leer.')
    args = argparser.parse_args()

    interprete = sys.executable

    p = subprocess.Popen([interprete, '-u', args.p], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    with open(args.t, 'r') as archivo:
        x = 1
        for linea in archivo:
            p.stdin.write(linea.encode())
            p.stdin.flush()
            
            respuesta = p.stdout.readline().decode().strip()
            print('Cantidad de palabras en la línea', x, ': ', respuesta)
            x += 1

    p.stdin.close()
    p.wait()

if __name__ == '__main__':
    Comunicador_Procesos()