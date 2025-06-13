import socket
def main():
    broker_host=' 0.0.0.0'
    broker_port=14000
    print("Publicador iniciado. Usa Formato : <topic> <mensaje>")
    while True:
        try:
            user_input= input(">> ")
            if user_input.lower()in ['exit', 'quit']:
                break
            
            topic, message = user_input.split(':', 1)
            msg = f"PUB:{topic}{message}"
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((broker_host, broker_port))
                sock.sendall(f"{topic} {message}".encode())
                respuesta = sock.recv(1024)
                print("Respuesta del broker:", respuesta.decode())
        except ValueError:
            print("Formato incorrecto. Use: <topic> <mensaje>")
        except Exception as e:
            print(f"[!] Error: {e}")
if __name__ == "__main__":
    main()
