import pygame
import os
import math
import time
import random

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = [ArcherTower(480,250), ArcherTower(850,500)]
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.timer = time.time()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= 4:
                self.timer = time.time()
                self.enemies.append(random.choice([Knight(), Swordsman(), Battleaxe()]))
                
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #Deleting enemies off the screen
            to_del = []
            for enemy in self.enemies:
                if enemy.x > 1130:
                    to_del.append(enemy)

            for d in to_del:
                self.enemies.remove(d)

            #Loop through towers
            for tower in self.towers:
                tower.attack(self.enemies)


            self.draw()
            

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))

        #draw enemies
        for enemy in self.enemies:
            enemy.draw(self.win)

        #draw towers
        for towers in self.towers:
            towers.draw(self.win)
        
        pygame.display.update()

class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.path = [(1110, 142), (1078, 142), (485, 144), (418, 162), (394, 197), (379, 240), (380, 282), (450, 328), (480, 340), (540, 350), (570, 390), (600, 448), (620, 500), (620, 560), (620, 561), (622, 562), (667, 563), (724, 563), (1026, 563), (1095, 563), (1150,563)]
        self.x = self.path[0][0]
        self.y = self.path [0][1]
        self.img = None
        self.path_pos = 0
        self.distance = 0
        self.imgs = []
        self.flipped = False
        self.max_health = 0

    def draw(self, win):
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 20))
        self.draw_health_bar(win)
        self.move()

    def draw_health_bar(self, win):
        length = 50
        move_by = round(length / self.max_health)
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.x - 15, self.y - 55, length, 10), 0)
        pygame.draw.rect(win, (0,255,0), (self.x - 15, self.y - 55, health_bar, 10), 0)

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

        direction = (x2-x1, y2-y1)
        length = math.sqrt((direction[0])**2 + (direction[1])**2)
        direction = (direction[0]/length, direction[1]/length)

        #Flips the image if it's moving in the positive x direction so it looks like it's walking in the correct direction
        if direction[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)
        elif direction[0] > 0 and self.flipped == True:
            self.flipped = False
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)
            
        
        move_x, move_y = ((self.x + direction[0]), (self.y + direction[1]))

        self.x = move_x
        self.y = move_y

        #Move point
        if direction[0] >= 0:
            if direction[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:
            if direction[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1


    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
        return False


knight_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    knight_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy4", "4_enemies_1_run_0" + add_str + ".png")), (64, 64)))
            
class Knight(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 1
        self.health = self.max_health
        self.imgs = knight_imgs
        

battleaxe_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    battleaxe_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy7", "7_enemies_1_run_0" + add_str + ".png")), (64, 64)))
    
class Battleaxe(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 5
        self.health = self.max_health
        self.imgs = battleaxe_imgs
        

swordsman_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    swordsman_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy10", "10_enemies_1_run_0" + add_str + ".png")), (64, 64)))
    
class Swordsman(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 3
        self.health = self.max_health
        self.imgs = swordsman_imgs


class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_imgs = []
        self.damage = 1

    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def sell(self):
        return self.sell_price[self.level-1]

    def upgrade(self):
        self.level += 1
        self.damage += 1

    def upgrade_cost(self):
        return self.price[self.level-1]

    def move(self, x, y):
        self.x = x
        self.y = y

class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 200
        self.in_range = False
        self.left = True
        self.timer = time.time()
        self.damage = 1

        #Archer tower
        for x in range(7,10):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")), (90, 90)))

        #Archer character
        for x in range(38,43):
            self.archer_imgs.append(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")))


    def draw(self, win):
        #Show range of tower (translucent)
        surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (255,135,135, 60), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        super().draw(win)

        if self.in_range == True:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs)*3:
                self.archer_count = 0

        else:
            self.archer_count = 0
            
        archer = self.archer_imgs[self.archer_count//3]
        if self.left == True:
            add = -25
        else:
            add = -archer.get_width() + 10
        win.blit(archer, ((self.x + self.width//2 + add), (self.y - archer.get_height() - 25)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        self.in_range = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if distance < self.range:
                self.in_range = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.x)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)

            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)


g = Game()
g.run()
