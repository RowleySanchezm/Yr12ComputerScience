import pygame

# -- Global Constants


# -- Colours

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame

pygame.init()


# -- Blank Screen

size = (640,480)
screen = pygame.display.set_mode(size)


# -- Title of new window/screen

pygame.display.set_caption("My Window")


# -- Exit game flag set to false

done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
