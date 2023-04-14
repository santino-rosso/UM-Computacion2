"""Escribir un programa en Python que comunique dos procesos. 
El proceso padre deberá leer un archivo de texto y enviar cada línea del archivo al proceso hijo a través de un pipe. 
El proceso hijo deberá recibir las líneas del archivo y, por cada una de ellas, contar la cantidad de palabras que contiene y mostrar ese número."""


import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, help='Nombre del archivo de texto.')
    args = parser.parse_args()
    
    ext_l, ext_e = os.pipe()
    pid = os.fork()

    if pid > 0:
        os.close(ext_l)
        with open(args.f, 'r') as a:
            for linea in a:
                os.write(ext_e, linea.encode())
        os.close(ext_e)
    else:
        os.close(ext_e)
        linea = os.read(ext_l, 1024).decode()
        linea = linea.splitlines()
        x = 1
        for palabras in linea:
            palabras = palabras.split()
            print('Cantidad de palabras en la línea', x, ': ', len(palabras))
            x += 1
        os.close(ext_l)

if __name__ == '__main__':
    main()