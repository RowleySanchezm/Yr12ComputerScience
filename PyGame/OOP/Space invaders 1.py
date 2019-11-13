import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE = (34, 20, 235)

class Invader(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height):
        #Call the parent class (Sprite) constructor
        super().__init__()

        #Create an image of block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        #Fetching the rectangle image
        self.rect = self.image.get_rect()
    #End function

    def reset_pos(self):
        #reset to a random position on top of the screen
        self.rect.y = random.randrange(-50, 0)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        # Move invader down one pixel
        self.rect.y += 1
 
        # If invader is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()
        #End if

class Player(Invader):
    #Derrives from block, but overrides the update function so that player block follows mouse
    def update(self):
        # Get the current mouse position
        pos = pygame.mouse.get_pos()

        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]


#Initialise Pygame
pygame.init()

#Set height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of sprites that have been grouped together (excludes player sprite)
invader_list = pygame.sprite.Group()
 
# This is a list of every sprite including the player sprite
all_sprites_list = pygame.sprite.Group()

#Creating 30 random invaders using a for loop
for i in range(30):
    # This represents an invader
    invader = Invader(BLUE, 20, 15)
 
    # Set a random location for the block
    invader.rect.x = random.randrange(screen_width)
    invader.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    invader_list.add(invader)
    all_sprites_list.add(invader)
#Next i

#Creating the player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(BLACK)

    #Calls update() method on every sprite in the list
    all_sprites_list.update()

    #See if the player block has collided with anthing
    invader_hit_list = pygame.sprite.spritecollide(player, invader_list, False)

    #Check the list of collisions
    for invader in invader_hit_list:
        score += 1
        print(score)

        #Reset the invader to top of screen to fall again
        invader.reset_pos()
    #Next block

    #Draw all the sprites
    all_sprites_list.draw(screen)
        
    #Limit to 20 frames per second
    clock.tick(20)

    #Update screen
    pygame.display.flip()

pygame.quit()
