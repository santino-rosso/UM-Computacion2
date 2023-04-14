"""Realizar un programa que implemente fork junto con el parseo de argumentos. 
Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa. 
El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa."""

import argparse
import math
import os


def calcular_raiz(num):
    raiz = math.sqrt(num)
    return raiz


def calculate_raiz_negativa(num):
    raiz_ne = -math.sqrt(num)
    return raiz_ne


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=float, help='Número al que se le desea calcular la raíz cuadrada.')
    parser.add_argument('-f', action='store_true', help='Indica si se debe realizar un fork.')
    args = parser.parse_args()

    if args.f:
        pid = os.fork()
        if pid > 0:
            x = os.getpid()
            print('Soy el padre, mi PID es', x)
            print('La raíz cuadrada positiva de', args.n, 'es: ', calcular_raiz(args.n))
        else:   
            x = os.getpid()
            print('Soy el hijo, mi PID es', x)
            print('La raíz cuadrada negativa de', args.n, 'es: ', calculate_raiz_negativa(args.n))
    else:
        x = os.getpid()
        print('Soy el padre, mi PID es', x)
        print('La raíz cuadrada de', args.n, 'es: ', calcular_raiz(args.n))  

          
if __name__ == '__main__':
    main()