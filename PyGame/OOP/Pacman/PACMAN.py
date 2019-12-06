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
size = (800, 800)
screen_height = 800
screen_width = 800
screen = pygame.display.set_mode(size)

class Wall(pygame.sprite.Sprite):
    def __init__(self,block_dimensions,colour):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([block_dimensions, block_dimensions])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
#        self.rect.x = x_position  # SRC - You have not set these as parameters
#        self.rect.y = y_position
    #end procedure
#end class

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

y_position = 0
f = open("maze.txt","rt")
### SRC - You need y_position = 0
data = f.read()  ### SRC - remove this line
for line in data: ### SRC - This should be - for line in f:
    y_position += 40  ### SRC - This line should go at the end of the loop
    x_position = 0
    for x_position in line: ### SRC - This should be - for item in line 
        if x_position == "w":  ### SRC - if item == "w"
            wall = Wall(40,LILAC)
            wall.rect.x = x_position
            wall.rect.y = y_position
            wall_group.add(wall)
            all_sprites_group.add(wall)
            x_position += 40 ### SRC - unindent this one tab

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
