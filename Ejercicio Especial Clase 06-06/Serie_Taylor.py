import threading
import math

def calcular_termino(x, n, resultados):
    termino = ((-1) ** n) * (x ** (2*n + 1)) / math.factorial(2*n + 1)
    lock.acquire()
    resultados.append(termino)
    lock.release()

def sumar_terminos(resultados):
    global resultado
    for resul in resultados:
        resultado += resul


if __name__ == '__main__':
    x = float(input("Ingrese el valor de x: "))
    while True:
        cantidad_terminos = int(input("Ingrese la cantidad de terminos: "))
        if cantidad_terminos > 0:
            break
    lock = threading.Lock()

    resultado = 0
    hilos = []
    resultados = []

    for n in range(cantidad_terminos):
        hilo = threading.Thread(target=calcular_termino, args=(x, n, resultados))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    hilo = threading.Thread(target=sumar_terminos, args=(resultados,))
    hilo.start()
    hilo.join()

    referencia = math.sin(x) 
    diferencia = resultado - referencia

    print("Resultado:", resultado)
    print("Diferencia:", diferencia)