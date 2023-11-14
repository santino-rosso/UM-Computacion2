import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='TP2 - Cliente imágenes')
    parser.add_argument('-i', '--ip', required=True, help='Dirección de escucha')
    parser.add_argument('-p', '--port', required=True, type=int, help='Puerto de escucha')
    parser.add_argument('-f', '--image', required=True, help='Direccion de la imagen')
    args = parser.parse_args()

    # Crear los datos de la solicitud
    files = {'image': open(args.image, 'rb')}

    if ':' in args.ip:
        # Enviar la solicitud POST al servidor
        response = requests.post(f'http://[{args.ip}]:{args.port}', files=files)
    else:
        response = requests.post(f'http://{args.ip}:{args.port}', files=files)

    # Guardar la imagen procesada
    with open('image_processed.png', 'wb') as processed_image_file:
        processed_image_file.write(response.content)

if __name__ == "__main__":
    main()
