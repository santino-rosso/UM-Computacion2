import os
import argparse
import sys 


parser = argparse.ArgumentParser()    
parser.add_argument('-f', '--file', type=str, help='Indicar el archivo de texto que se quiere utilizar.')
args, unknown = parser.parse_known_args()             # Se guardan los argumentos reconocidos y los no reconocidos.

if unknown:                                           # Si hay argumentos no reconocidos, se cierra el programa.
    print("Argumentos no reconocidos")
    exit()

try:
    with open(args.file, "r") as archivo:
        lineas = archivo.readlines()
        numero_de_lineas = len(lineas)
    archivo.close()
except (FileNotFoundError, PermissionError):
    print("El archivo no existe o no se puede abrir.")
    exit()

archivo_invertido = []

for i in lineas:
    l_padre, e_hijo = os.pipe()
    l_hijo, e_padre = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(l_padre)  
        os.close(e_padre)
        try:
            linea = os.read(l_hijo, 1024).decode('utf-8')
        except (UnicodeDecodeError) :
            print("Error al decodificar el mensaje.")
            exit()
        os.close(l_hijo)
        linea_invertida = linea[::-1]
        try:
            os.write(e_hijo, linea_invertida.encode('utf-8'))
        except (UnicodeEncodeError):
            print("Error al codificar el mensaje.")
            exit()            
        os.close(e_hijo)
        sys.exit(0)
    else:
        os.close(l_hijo)
        os.close(e_hijo)
        mensaje = i.strip()
        try:  
            os.write(e_padre, mensaje.encode('utf-8'))
        except (UnicodeEncodeError):
            print("Error al codificar el mensaje.")
            exit()
        os.close(e_padre)
        try:
            mensaje_hijo = os.read(l_padre, 1024).decode('utf-8').strip()
        except (UnicodeDecodeError):
            print("Error al decodificar el mensaje.")
            exit()
        os.close(l_padre)
        archivo_invertido.append(mensaje_hijo)

for x in archivo_invertido:
    print(x)
    
    




