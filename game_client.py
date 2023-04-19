import pygame
import socket
import time

pygame.init()

# defy colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the button surface and text
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Click game")
button_width = 10
button_height = 10
button = pygame.Surface((button_width, button_height))
button.fill(GREEN)

# connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

while True:
    try:
        client_socket.send("send".encode())
        response = client_socket.recv(1024).decode().split(",")
        button_x = int(response[0])
        button_y = int(response[1])
        screen.fill(BLACK)
        screen.blit(button, (button_x, button_y))
        pygame.display.flip()
        time.sleep(0.1)

        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            quit()

        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()

            if button_x <= mouse_pos[0] <= button_x + button_width and button_y <= mouse_pos[1] <= button_y + \
                    button_height:
                client_socket.send("got it".encode())
                print(f'Current score is {response[2]}')
    except ConnectionAbortedError:
        print("Server connection closed. Exiting...")
        pygame.quit()
        quit()
