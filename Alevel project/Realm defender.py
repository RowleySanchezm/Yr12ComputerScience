import pygame
import os
import math

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.draw()
            

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))
        pygame.display.update()

class Enemy:
    imgs = []
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.velocity = 3
        self.path = [(1078, 142), (485, 144), (418, 162), (394, 197), (379, 240), (380, 282), (401, 328), (438, 355), (481, 370), (528, 390), (554, 428), (563, 461), (572, 500), (586, 546), (622, 575), (667, 583), (724, 582), (1026, 584), (1095, 582)]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.distance = 0

    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        x1, y2 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1120, 582)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        self.move_count += 1
        direction = (x2-x1, y2-y1)
        
        move_x, move_y = (self.x + direction[0] * self.move_count, self.y + direction[1] * self.move_count)
        self.distance += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)

        if self.distance >= move_distance:
            self.distance = 0
            self.move_count = 0
            self.path_pos += 1
        

        self.x = move_x
        self.y = move_ y

            

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True


g = Game()
g.run()
