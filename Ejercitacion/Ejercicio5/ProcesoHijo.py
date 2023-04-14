import sys

for linea in sys.stdin:
    contar = len(linea.split())
    print(contar)
    
    sys.stdout.flush()