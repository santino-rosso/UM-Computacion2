"""1- Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar."""
### Solucion 1 ###
import sys
import getopt  

(opts, args) = getopt.getopt(sys.argv[1:], 'n:')
for (opt, arg) in opts:
    if opt == '-n':
        n = int(arg)
        lis = []
        if n > 0:
            for x in range(n*2):
                if x%2 == 1:
                    lis.append(x)
            print (lis)
        else:
            print ("El numero debe ser positivo")



