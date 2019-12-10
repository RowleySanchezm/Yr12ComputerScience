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
        self.colour = colour
        self.image = pygame.Surface([block_dimensions, block_dimensions])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if pygame.sprite.spritecollide(player,wall_group,False):
                player.rect.x += 0
            else:
                player.rect.x -= 4
            #end if
        #end if
        if keys[pygame.K_RIGHT]:
            if pygame.sprite.spritecollide(player,wall_group,False):
                player.rect.x += 0
            else:
                player.rect.x += 4
            #end if
        #end if
        if keys[pygame.K_UP]:
            if pygame.sprite.spritecollide(player,wall_group,False):
                player.rect.y += 0
            else:
                player.rect.y -= 4
            #End if
        #End if
        if keys[pygame.K_DOWN]:
            if pygame.sprite.spritecollide(player,wall_group,False):
                player.rect.y += 0
            else:
                player.rect.y += 4
            #End if
        #End if
    #End function
        

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()

# -- Title of new window/screen
pygame.display.set_caption("Pacman")

game_over = False

#Sprite groups
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
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
        #End if
        x_position += 30
    #Next item
    y_position += 30
#Next Line
f.close()

player = Player(20, YELLOW)
all_sprites_group.add(player)
player_group.add(player)


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event

    #Calls update() method on every sprite
    player_group.update()
            
            
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
