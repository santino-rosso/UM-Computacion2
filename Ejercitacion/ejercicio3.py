"""3- Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. Esta última opción no debe ser obligatoria. Si hubiese errores deben guardarse en un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error."""
import sys
import getopt
import os


try:
    (opts, args) = getopt.getopt(sys.argv[1:], 'f:p:')
    for (opt, arg) in opts:

        archivo = arg
        if os.path.isfile(archivo):
            with open(archivo, "r") as f:
                texto = f.read()
                palabras = texto.split()
                lineas = texto.splitlines()
                suma = 0
                for palabra in palabras:
                    suma += len(palabra)

        if opt == '-f':
            print ("Numero de palabras: ", len(palabras))
            print ("Numero de lineas: ", len(lineas))

        if opt == '-p':
            print ("Longitud promedio de palabras: ", round(suma/len(palabras)))
            
except:
    with open("errors.log", "w") as f:
        f.write("Error: " + str(sys.exc_info()[0]))
