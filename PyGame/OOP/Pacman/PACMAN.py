import pygame
import sys
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
LILAC = (216,104,250)

# -- Blank Screen
size = (600, 600)
screen_height = 600
screen_width = 600
screen = pygame.display.set_mode(size)

class Wall(pygame.sprite.Sprite):
    def __init__(self,block_dimensions,colour):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([block_dimensions, block_dimensions])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        x_position = 0
        y_position = 0
        self.rect.x = x_position
        self.rect.y = y_position
    #end procedure
#end class

class Player(pygame.sprite.Sprite):
    def __init__(self,block_dimensions,colour):
        super().__init__()
        

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Title of new window/screen
pygame.display.set_caption("Pacman")

game_over = False

#Sprite groups
wall_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()

f = open("maze.txt","rt")
y_position = 0
for line in f:
    x_position = 0
    for item in line:
        if item == "w":
            wall = Wall(30,BLUE)
            wall.rect.x = x_position
            wall.rect.y = y_position
            wall_group.add(wall)
            all_sprites_group.add(wall)
        x_position += 30
    y_position += 30

### SRC - f.close()
        

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
            
            
    # -- Game logic goes after this comment

        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    

    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
