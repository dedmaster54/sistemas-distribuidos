import socket

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(('localhost',8080))
cliente_socket.sendall(b"hola desde el cliente ")
respuesta = cliente_socket.recv(1024)
print("respuesta del servidor:",respuesta.decode())
cliente_socket.close()
