"""## EJERCICIOS ##
En el ejercicio de la clase 15 se proponía el siguiente ejercicio:

**Realizar dos versiones de un servidor de mayúsculas que atienda múltiples clientes de forma concurrente utilizando multiprocessing y threading utilizando sockets TCP.**

1- Actualizar el servidor para que sea un servidor asincrónico."""

import asyncio
import signal

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

async def managment_client(reader, writer):
    while True:
        data = await reader.read(1024)
        if data.strip().lower() == b'exit' or data == b'':
            break
        answer = data.upper()
        writer.write(answer)
        await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    host = "127.0.0.1"  
    port = 30501

    server = await asyncio.start_server(managment_client, host, port)
    
    async with server:
        await server.serve_forever()

    

if __name__ == "__main__":
    asyncio.run(main())





