import socket
import pyautogui
import threading


def handle_client(sock, addr):
    print(f"Received connection from {addr}")
    while True:
        data = sock.recv(1024)
        x, y = data.decode().split(",")
        x = int(x)
        y = int(y)
        pyautogui.moveTo(x, y)
        response = "OK"
        sock.send(response.encode())


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
