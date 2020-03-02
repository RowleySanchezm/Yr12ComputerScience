import pygame
import os
import math

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Knight(), Battleaxe()]
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            pygame.time.delay(100)
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #Deleting enemies off the screen
            to_del = []
            for enemy in self.enemies:
                if enemy.x > 1105:
                    to_del.append(enemy)

            for d in to_del:
                self.enemies.remove(d)


            self.draw()
            

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))

        #draw enemies
        for enemy in self.enemies:
            enemy.draw(self.win)
        
        pygame.display.update()

class Enemy:
    imgs = []
    
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.velocity = 3
        self.path = [(1078, 142), (485, 144), (418, 162), (394, 197), (379, 240), (380, 282), (401, 328), (438, 355), (481, 370), (528, 390), (554, 428), (563, 461), (572, 500), (586, 546), (622, 575), (667, 583), (724, 582), (1026, 584), (1095, 582), (1150,582)]
        self.x = self.path[0][0]
        self.y = self.path [0][1]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.distance = 0

    def draw(self, win):
        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs)*3:
            self.animation_count = 0
            
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1120, 582)
        else:
            x2, y2 = self.path[self.path_pos+1]

        move_distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        self.move_count += 1
        direction = (x2-x1, y2-y1)
        
        move_x, move_y = ((self.x + direction[0] * self.move_count), (self.y + direction[1] * self.move_count))
        self.distance += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)

        #Move point
        if self.distance >= move_distance:
            self.distance = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False

        self.x = move_x
        self.y = move_y
        return True 


    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True

class Knight(Enemy):
    imgs = []

    for x in range(20):
        add_str = str(x)
        if x < 10:
            add_str = "0" + add_str
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy4", "4_enemies_1_run_0" + add_str + ".png")), (64, 64)))

    def __init__(self):
        super().__init__()


class Battleaxe(Enemy):
    imgs = []

    for x in range(20):
        add_str = str(x)
        if x < 10:
            add_str = "0" + add_str
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy7", "7_enemies_1_run_0" + add_str + ".png")), (64, 64)))

    def __init__(self):
        super().__init__()

g = Game()
g.run()
