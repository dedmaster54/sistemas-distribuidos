import argparse
from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process, Queue
import time


def worker(task_queue):
    while True:
        try:
            conn, addr = task_queue.get()
            print(f"Procesando la solicitud de {addr}")
            data = conn.recv(1024)
            print(f"Datos recibidos de {addr}: {data.decode()}")
            conn.sendall(b"respuesta del servidor")
            conn.close()
        except Exception as e:
            print(f"Error al procesar la solicitud: {e}")
        time.sleep(0.1)


def start_server(host='localhost', port=8080):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Servidor ejecutándose en {host}:{port}...")

    task_queue = Queue()

    workers = [Process(target=worker, args=(task_queue,)) for _ in range(2)]  # Usa más de 1 worker si lo deseas
    for w in workers:
        w.daemon = True
        w.start()

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Conexión aceptada de {addr}")
            task_queue.put((conn, addr))
    except KeyboardInterrupt:
        print("Servidor detenido por el usuario.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP")
    parser.add_argument("port", type=int, help="Puerto de escucha")
    args = parser.parse_args()

    start_server(port=args.port)
# Este es un servidor que utiliza multiprocessing para manejar múltiples conexiones simultáneamente.


    
