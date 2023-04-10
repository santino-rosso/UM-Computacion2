"""2- Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número entero. El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero."""
### Solucion 2 ###
import sys
import getopt
(opts, args) = getopt.getopt(sys.argv[1:], 't:n:')
for (opt, arg) in opts:
    if opt == '-t':
        texto = arg 
    if opt == '-n':
        numero = int(arg)
        if numero >= 0:
            for x in range(numero):
                print (texto, end="")
            print ("")
        else:
            print ("El numero debe ser positivo")