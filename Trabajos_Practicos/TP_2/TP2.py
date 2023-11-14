import http.server
import multiprocessing
from PIL import Image
import io
import argparse
import cgi
import socketserver
import socket

def process_image(q, e):
    try:
        image_data = q.get()
        with io.BytesIO(image_data) as image_buffer:
            print("Abriendo la imagen...")
            image = Image.open(image_buffer).convert('L')

        with io.BytesIO() as buffer:
            print("Guardando la imagen procesada...")
            image.save(buffer, format='PNG')
            processed_image_data = buffer.getvalue()

        q.put(processed_image_data)
        e.set()
        print("Procesamiento de imagen terminado.")

    except Exception as error:
        print(f"Error al procesar la imagen: {error}")
        e.set()


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_type, _ = cgi.parse_header(self.headers['Content-Type'])

            if content_type == 'multipart/form-data':
                form_data = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                if 'image' in form_data:
                    image_field = form_data['image']
                    if image_field.file:
                        image_data = image_field.file.read()

                        q = multiprocessing.Queue()
                        e = multiprocessing.Event()
                        p = multiprocessing.Process(target=process_image, args=(q, e))
                        p.start()
                        q.put(image_data)
                        e.wait()
                        image_data = q.get()

                        self.send_response(200)
                        self.send_header('Content-type', 'image/png')
                        self.end_headers()
                        self.wfile.write(image_data)
                        return

            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Error en la solicitud')

        except Exception as error:
            print(f"Error en la solicitud: {error}")
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f'Error interno del servidor: {error}')


class MyThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    def server_bind(self):
        for res in socket.getaddrinfo(self.server_address[0], self.server_address[1], socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                self.socket = socket.socket(af, socktype, proto)
                if hasattr(self.socket, 'setsockopt'):
                    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket.bind(sa)
                self.server_address = self.socket.getsockname()
                break
            except OSError:
                if self.socket:
                    self.socket.close()
                self.socket = None
                continue
        if self.socket is None:
            raise Exception("No se pudo enlazar con el servidor")


def main():
    parser = argparse.ArgumentParser(description='TP2 - Procesa imágenes')
    parser.add_argument('-i', '--ip', required=True, help='Dirección de escucha')
    parser.add_argument('-p', '--port', required=True, type=int, help='Puerto de escucha')
    args = parser.parse_args()

    server_address = (args.ip, args.port)
    httpd = MyThreadingHTTPServer(server_address, MyHandler)

    print(f"Servidor en ejecución en http://{args.ip}:{args.port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
        httpd.shutdown()
        httpd.server_close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()