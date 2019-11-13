import pygame
import random
# -- Global Constants

WIDTH = 640
HEIGHT = 480
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
COLOURS = [(182,53,182),
           (23,243,60),
           (4,224,249),
           (255,0,0),
           (255,255,0),
           (50,50,255)]

# -- My Classes

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_x = random.randint(1, 9)
        self.direction_y = random.randint(1, 9)
        self.colour = random.choice(COLOURS)
        self.radius = random.randint(5,20)
        
    def move(self):
        if self.x >= WIDTH-15 or self.x <= 0+15:
            self.direction_x *= -1
        if self.y >= HEIGHT-15 or self.y <= 0+15:
            self.direction_y *= -1
        self.y += self.direction_y
        self.x += self.direction_x

    def draw(self):
        pygame.draw.circle(screen, self.colour, (block.x, block.y), self.radius)
    
# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Screen of bouncing balls")

game_over = False
blocks = []
for count in range(50):
    blocks.append(Ball(random.randint(0, 640),random.randint(0, 480)))
#next count

### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

            
    # -- Game logic goes after this comment
    for block in blocks:
        block.move()
    #next block
    
        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    for block in blocks:
        block.draw()
    #next block


    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()
