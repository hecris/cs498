from collections import Counter
import numpy as np
import random

def is_derangement(arr):
    return not any (i==x for i, x in enumerate(arr))

def generate_derangement(n):
    a = list(np.random.permutation(n))
    while not is_derangement(a):
        a = list(np.random.permutation(n))
    return a

def generate_swap(arr):
    bag = [i for i, x in enumerate(arr) if x != i]
    if not bag:
        return -1, -1
    i = random.choice(bag)
    j = random.choice(bag)

    while (i == j):
        i = random.choice(bag)
        j = random.choice(bag)

    return i, j



# Import and initialize the pygame library
import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 500])
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Run until the user asks to quit
running = True
N = int(input('N: '))
arr = generate_derangement(N)
FONT = pygame.font.SysFont('Arial', 25)
swaps = 0
total_swaps_avg = 0
total_swaps = 0
runs = 0
counter = Counter()

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    start = 10
    pos = start
    BOX_SIZE = 50
    # Draw a solid blue circle in the center
    rect_objs = []
    for i, x in enumerate(arr):
        color = BLUE if i == x else BLACK
        rect_obj = pygame.draw.rect(screen, (color), (pos, 250, BOX_SIZE, BOX_SIZE), 2)
        rect_objs.append(rect_obj)
        text_surface_object = FONT.render(str(x), True, color)
        text_rect = text_surface_object.get_rect(center=rect_obj.center)
        screen.blit(text_surface_object, text_rect)
        pos += BOX_SIZE

    i, j = generate_swap(arr)
    if i != -1:
        swap_type = int(arr[j] == i) + int(arr[i] == j)
        counter[swap_type] += 1
        arr[i], arr[j] = arr[j], arr[i]
        swaps += 1
        total_swaps += 1
        rect_obj = pygame.draw.rect(screen, (RED), (start + BOX_SIZE * i, 250, BOX_SIZE, BOX_SIZE), 2)
        rect_obj = pygame.draw.rect(screen, (RED), (start + BOX_SIZE * j, 250, BOX_SIZE, BOX_SIZE), 2)

    screen.blit(FONT.render('swaps: {}'.format(swaps), True, BLACK), (0,0))
    if runs > 0:
        screen.blit(FONT.render('avg: {}'.format(total_swaps_avg / runs), True, BLACK), (0,30))
    screen.blit(FONT.render('runs: {}'.format(runs), True, BLACK), (0,60))
    if total_swaps > 0:
        screen.blit(FONT.render('0-swaps: {}/{}={}'.format(counter[0],total_swaps,counter[0]/total_swaps), True, BLACK), (0,90))
        screen.blit(FONT.render('1-swaps: {}/{}={}'.format(counter[1],total_swaps,counter[1]/total_swaps), True, BLACK), (0,120))
        screen.blit(FONT.render('2-swaps: {}/{}={}'.format(counter[2],total_swaps,counter[2]/total_swaps), True, BLACK), (0,150))


    # Flip the display
    pygame.display.flip()
    pygame.time.wait(1000)
    if i == -1:
        pygame.time.wait(1000)
        runs += 1
        total_swaps_avg += swaps
        arr = generate_derangement(N)
        swaps = 0
    # time.sleep(1)

# Done! Time to quit.
pygame.quit()
