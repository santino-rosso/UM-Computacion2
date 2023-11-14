from multiprocessing import Pipe, Process
import argparse 


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

def invertir(conexion):
    linea = conexion.recv()
    linea_invertida = linea[::-1]
    conexion.send(linea_invertida)
    conexion.close()

for i in lineas:
    conexion_padre, conexion_hijo = Pipe()
    proceso_hijo = Process(target=invertir, args=(conexion_hijo,))
    proceso_hijo.start()
    mensaje = i.strip()
    conexion_padre.send(mensaje)
    proceso_hijo.join()
    respuesta = conexion_padre.recv()
    conexion_padre.close()
    archivo_invertido.append(respuesta)

for x in archivo_invertido:
    print(x)
    
    