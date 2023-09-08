# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Run until the user asks to quit
running = True
arr = [1,2,3]
FONT = pygame.font.SysFont('Arial', 25)

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    pos = 10
    BOX_SIZE = 30
    # Draw a solid blue circle in the center
    for x in arr:
        rect_obj = pygame.draw.rect(screen, (BLACK), (pos, 250, BOX_SIZE, BOX_SIZE), 2)
        text_surface_object = FONT.render(str(x), True, BLACK)
        text_rect = text_surface_object.get_rect(center=rect_obj.center)
        screen.blit(text_surface_object, text_rect)
        pos += BOX_SIZE + 1

    # Flip the display
    pygame.display.flip()
    time.sleep(1)

# Done! Time to quit.
pygame.quit()
