"""## EJERCICIOS ##
1 - Implementar un buscador de número primos. Deberá encontrar el número primo inmediátamente inferior a un valor dado.
Debe implementarse utilizando concurrent.futures.

Deberán lanzarse distintos procesos que vayan probando desde 2 hasta el valor dado con pasos diferentes para maximizar la posibilidad de encuentro en el menor tiempo."""

from concurrent.futures import ProcessPoolExecutor
import os

def primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

if __name__ == "__main__":

    while True:
        valor = int(input("Ingrese un valor mayor a uno: "))
        print("")
        if valor > 1:
            break
        
    num_cpus = os.cpu_count()
    workers = min(num_cpus, valor)

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futuros = {}
        for n in reversed(range(2, valor + 1)):  
            futuros[n] = executor.submit(primo, n)
            
        for n, futuro in futuros.items():
            if futuro.result() and (n + 1 > valor or not futuros[n + 1].result()):
                print("El número primo inmediatamente inferior a " + str(valor) + " es " + str(n))
                break