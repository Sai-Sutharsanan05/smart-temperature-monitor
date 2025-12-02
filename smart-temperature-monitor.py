import pygame
import random
import threading
import time
import sys
pygame.init()
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Temperature Monitor")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
temperature = 25.0
running = True
font_large = pygame.font.SysFont("Arial", 40)
font_small = pygame.font.SysFont("Arial", 24)
def simulate_temperature():
    global temperature
    while running:
        # Randomly vary temperature between 10°C and 40°C
        temperature = round(random.uniform(10, 40), 1)
        time.sleep(2)  # update every 2 seconds
thread = threading.Thread(target=simulate_temperature)
thread.start()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill(WHITE)

    # Display temperature
    temp_text = font_large.render(f"{temperature} °C", True, BLACK)
    screen.blit(temp_text, (WIDTH//2 - temp_text.get_width()//2, HEIGHT//2 - 50))

    # Display status
    if temperature < 15:
        status_text = font_small.render("Too Cold!", True, BLUE)
    elif temperature > 35:
        status_text = font_small.render("Too Hot!", True, RED)
    else:
        status_text = font_small.render("Normal Range", True, GREEN)
    screen.blit(status_text, (WIDTH//2 - status_text.get_width()//2, HEIGHT//2 + 20))

    pygame.display.update()
    clock.tick(30)
