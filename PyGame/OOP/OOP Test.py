import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_text(surf, text, size, x, y): 
    font = pygame.font.SysFont("comicsansms",20)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#End function

### What is a class?
###A class is a 'blueprint' for an object and it defines the attributes and behaviours of objects in that class by using methods. The method is the fucntionality of the class whilst an attribute is data asscoiated with the class.
 
class Block(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        ### What is this subroutine known as?
        ###This is the constructor which is used to create the actual objects when instantiated.
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour) 
        self.rect = self.image.get_rect()
    #end function
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
    #end function

    def update(self):
        #Move block down the screen
        self.rect.y += 1

        #Reset block to top if it hits the bottom
        if self.rect.y > 410:
            self.reset_pos()
        #End if
    #End function
#end class



 
### Fix this class so that it inherits Block and is the colour RED
class Player(Block):
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
     #end function
#end class
        
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
block_hit_group = pygame.sprite.Group()
 

### Create 50 random positioned blocks that will be displayed

for b in range(50):
    #Instantiate block
    block = Block(BLACK, 10, 10)
    
    #Random position
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    #Add to lists
    block_list.add(block)
    all_sprites_list.add(block)
#Next b
 
# Create a red player 
player = Player(RED, 20, 20)
player.rect.y = screen_width // 2
player.rect.x = screen_height
all_sprites_list.add(player)

game_over = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End if
    #Next event
 
    #Clear the screen
    screen.fill(WHITE)
 
    #Calls update() method on every sprite in the list
    
    all_sprites_list.update()
    
    ###What OOP concept is being used here?
    ###Encapsulation is being used
    
    #See if the player has collided with a block.
    block_hit_group = pygame.sprite.spritecollide(player, block_list, True)

    #Draw score
    draw_text(screen, 'SCORE: ' + str(score), 18, 40, 10)
    
    #Update the score +1 for every block collision
    for block in block_hit_group:
        score += 1
    #next block
    
    #Draw all the spites
    all_sprites_list.draw(screen)
    block_list.draw(screen)
 
    #Limit to 20 frames per second
    clock.tick(20)
 
    #Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()
