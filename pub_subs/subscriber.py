import socket
import threading
def listen_to_broker(sock):
    try:
        while True:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
    except:
        print("[!]CONEXION CERRADA POR EL BROKER : ")
def main():
    broker_host = 'localhost'
    broker_port = 1400
    topic =input("Tema a suscribirse: ").strip()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((broker_host, broker_port))
    sock.sendall(f"SUB:{topic}".encode())
    print(f"[SUSCRIPTOR] Suscrito a: {topic}. Esperando mensajes...")
    threading.Thread(target=listen_to_broker, args=(sock,), daemon=True).start()
    try:
        while True:
            pass #Mantener activo 
    except KeyboardInterrupt:
        print("Saliendo...")
        sock.close()
if __name__ == "__main__":
    main()