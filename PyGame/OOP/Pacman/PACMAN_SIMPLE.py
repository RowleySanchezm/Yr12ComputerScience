import pygame
from math import atan, cos, sin
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
LILAC = (216,104,250)

# -- Blank Screen
screen_height = 600
screen_width = 600
size = (screen_height, screen_width)
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

        #Set speed vectors
        self.walls = None
        self.change_x = 0
        self.change_y = 0
    #End procedure
        
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    #End procedure
 
    def update(self):
        # Move left/right
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            #End if
        #Next block
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            #End if
        #Next block
    #End function
#End class

class Ghost(pygame.sprite.Sprite):
    def __init__(self,block_dimensions,colour):
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface([block_dimensions, block_dimensions])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 540
        self.walls = None
    #End procedure

    def update(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            #End if
        #Next block
 
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.rect.y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            #End if
        #Next block
    #End function

    def moveghost():
        opposite = Player.rect.y - self.rect.y
        adjacent = Player.rect.x - self.rect.x
        angle = atan(opposite/adjacent)
        if self.rect.x > Player.rect.x:
            angle += 180
        #End if

        velocity = 3
        vx = velocity * cos(angle)
        vy = velocity * sin(angle)

        self.rect.x += vx
        self.rect.y += vy
    #End function
#End class

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
ghost_sprites_group = pygame.sprite.Group()

f = open("Maze.txt","rt")
y_position = 0
node_count = 0
vertex_count = 0
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
player.walls = wall_group
all_sprites_group.add(player)
player_group.add(player)
ghost = Ghost(30, RED)
ghost_sprites_group.add(ghost)


### -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
        #End If
    #Next event

    #Calls update() method on every sprite
    all_sprites_group.update()
    ghost_sprites_group.update()
            
    # -- Game logic goes after this comment

        
    # -- Screen background is BLACK
    screen.fill (BLACK)

    # -- Draw here
    all_sprites_group.draw(screen)
    ghost_sprites_group.draw(screen)
    

    
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#End While - End of game loop

pygame.quit()

