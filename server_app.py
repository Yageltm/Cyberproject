import socket
import threading

import pyautogui

pyautogui.FAILSAFE = False


def check_valid(position):
    sizes = list(pyautogui.size())
    if position[0] < 0:
        position[0] = 0
    if position[1] < 0:
        position[1] = 0
    if position[0] > sizes[0]:
        position[0] = sizes[0]
    if position[1] > sizes[1]:
        position[1] = sizes[1]
    return position


def use_tcp():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('TCP HOST IP:', host_ip)
    port = 3456
    socket_address = (host_ip, port)
    server_socket.bind(socket_address)
    server_socket.listen()
    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024).decode().split(',')
        if data[0] == 'right':
            pyautogui.click(button='right')
        elif data[0] == 'left':
            pyautogui.click()

        client_socket.close()


def use_udp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('UDP HOST IP:', host_ip)
    port = 5555
    sock.bind((host_ip, port))
    while True:
        data, addr = sock.recvfrom(1024)
        cur_x, cur_y = pyautogui.position()
        diffs = data.decode().split(',')
        print(diffs)
        move = [cur_x+int(diffs[0])*3, cur_y+int(diffs[1])*3]
        pyautogui.moveTo(move[0], move[1], 0.2)


tcp_thread = threading.Thread(target=use_tcp)
udp_thread = threading.Thread(target=use_udp)


def main():
    udp_thread.start()
    tcp_thread.start()
    udp_thread.join()
    tcp_thread.join()


main()
