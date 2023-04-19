import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))
while True:
    x = random.randint(0, 1365)
    y = random.randint(0, 767)

    coordinates = f"{x},{y}"
    client_socket.send(coordinates.encode())

    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")
