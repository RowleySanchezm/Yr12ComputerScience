import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE = (34, 20, 235)
YELLOW = (252, 240, 80)


def draw_text(surf, text, size, x, y): 
    font = pygame.font.SysFont("comicsansms",20)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#End function

def game_over(surf, text, size, x, y): 
    font = pygame.font.SysFont("comicsansms",50)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#End function


class Invader(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height):
        #Call the parent class (Sprite) constructor
        super().__init__()

        #Create an image of block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.x_direction = 1

        #Fetching the rectangle image
        self.rect = self.image.get_rect()
    #End function

    def reset_pos(self):
        #reset to a random position on top of the screen
        self.rect.y = random.randrange(-50, 0)
        self.rect.x = random.randrange(0, screen_width)
    #End function
 
    def update(self):
        # Move invader across one pixel
        self.rect.x += self.x_direction
 
        # If invader is too far down, reset to top of screen.
        if self.rect.y > 410:
            self.reset_pos()
        #End if
        if self.rect.x >= screen_width - 10:
            self.x_direction *= -1
            self.rect.y += 40
        elif self.rect.x <= 0:
            self.x_direction *= -1
            self.rect.y += 40
        #End if
            
    #End function

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([30, 10])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.speed = 8
        self.bullet_count = 75
        self.centre = 30 // 2
    #End function 
        
    
    #Makes it moves left and right 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player.rect.x <= 0:
                player.rect.x += 0
            else:
                player.rect.x -= 5
            #end if
        #end if
        if keys[pygame.K_RIGHT]:
            if player.rect.x >= 700 - 30:
                player.rect.x += 0
            else:
                player.rect.x += 5
            #end if
        #end if
    #End function

    def bullet_count(self):
        self.bullet_count -= 1
    #End function

class Bullet(pygame.sprite.Sprite):
    

    def __init__(self, colour, width, height):
        super().__init__()
        #Create an image of block
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        #Fetching the rectangle image
        self.rect = self.image.get_rect()
        self.speed = 6
    #End function

    def update(self):
        # Moving bullet up the screen
        self.rect.y -= self.speed
    #End function


#Initialise Pygame
pygame.init()

#X and Y coordinates
invader_x_coord = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650,
                    50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]
invader_y_coord = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                    40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40]

#Set height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of sprites that have been grouped together (excludes player sprite)
invader_list = pygame.sprite.Group()
 
# This is a list of every sprite including the player sprite
all_sprites_list = pygame.sprite.Group()

#Creating 26 random invaders using a for loop
for i in range(26):
    # This represents an invader
    invader = Invader(BLUE, 10, 10)
 
    # Set a random location for the block
    invader.rect.x = invader_x_coord[i-1]
    invader.rect.y = invader_y_coord[i-1]
 
    # Add the block to the list of objects
    invader_list.add(invader)
    #all_sprites_list.add(invader)
#Next i

#Creating the player block
player = Player()
player.rect.y = 380
all_sprites_list.add(player)

#Creating lists for bullets
bullet_group = pygame.sprite.Group()
bullet_hit_group = pygame.sprite.Group()


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

    #Set values
lives = 5
score = 0


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        #End if
    #Next event

    
    #Creating bullets
    keys = pygame.key.get_pressed()
    if player.bullet_count > 0 and keys[pygame.K_UP]:
        player.bullet_count -= 1
        bullet = Bullet(RED, 2, 2)

        #Bullet comes from player
        bullet.rect.x = player.rect.x + player.centre
        bullet.rect.y = player.rect.y

        #Add bullets to appropiate list
        bullet_group.add(bullet)
        #all_sprites_list.add(bullet)
    #End if

        
    # Clear the screen
    screen.fill(BLACK)
    
    #Calls update() method on every sprite in the list
    all_sprites_list.update()
    invader_list.update()
    bullet_group.update()

    #See if bullets have hit any invaders
    bullet_hit_group = pygame.sprite.groupcollide(bullet_group, invader_list, True, True)


    #See if the player block has collided with anthing
    invader_hit_list = pygame.sprite.spritecollide(player, invader_list, False)

    #Check the player for collisions then update lives and score
    draw_text(screen, 'LIVES: ' + str(lives), 18, screen_width // 6, 15)
    draw_text(screen, 'SCORE: ' + str(score), 18, screen_width // 6, 30)
    draw_text(screen, 'BULLET COUNT: ' + str(player.bullet_count), 18, screen_width // 6, 45)

    for bullet in bullet_hit_group:
        score += 10
    #next bullet

    for invader in invader_hit_list:
        lives -= 1
        score -= 50
        #Reset the invader to top of screen to fall again
        invader.reset_pos()
    #Next invader
    
    #Draw all the sprites
    all_sprites_list.draw(screen)
    invader_list.draw(screen)
    bullet_group.draw(screen)

    #Game over display
    if lives <= 0:
        game_over(screen, 'GAME OVER', 50, screen_width // 2, screen_height // 2)
    #End if
        
    #Limit to 20 frames per second
    clock.tick(20)

    #Update screen
    pygame.display.flip()
    
#End while

pygame.quit()
