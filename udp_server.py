import socket
import pyautogui
pyautogui.FAILSAFE = False
first = []
last = []


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


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('UDP HOST IP:', host_ip)
port = 3456
socket_address = (host_ip, port)
server_socket.bind(socket_address)

while True:
    data, address = server_socket.recvfrom(1024)
    data = data.decode().split(',')
    if data[0] == 'right':
        pyautogui.click(button='right')
    elif data[0] == 'left':
        pyautogui.click()
    elif data[0].startswith('n'):
        last = data
        last[0] = int(last[0][1:])
        last[1] = int(last[1])
        move = [last[0] - first[0], last[1] - first[1]]
        new_pos = [int(pos[0] + move[0] * 3), int(pos[1] + move[1] * 3)]
        new_pos = check_valid(new_pos)
        pyautogui.moveTo(new_pos[0], new_pos[1], 0.3)
    else:
        pos = pyautogui.position()
        first = data
        first[0] = int(first[0])
        first[1] = int(first[1])

server_socket.close()
