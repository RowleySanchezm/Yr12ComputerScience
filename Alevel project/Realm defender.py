import pygame
import os
import math
import time
import random

pygame.font.init()
lives_img = pygame.image.load(os.path.join("Game_images/GameInterface","heart.png"))
#Tower menu images
tower_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","menu2.png")), (150, 500))
range_support_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","range_support.png")), (75, 75))
attack_support_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","attack_support.png")), (75, 75))
powerful_archer_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","powerful_archer.png")), (75, 75))
quick_archer_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","quick_archer.png")), (75, 75))

support_tower_names = ["damage_object", "range_object"]
attack_tower_names = ["powerful_archer", "quick_archer"]

class Game:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = [QuickArcherTower(480,250), PowerfulArcherTower(850,490), PowerfulArcherTower(850,250)]
        self.support_towers = [DamageTower(560,300)]
        self.lives = 10
        self.money = 20000
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.timer = time.time()
        self.font = pygame.font.SysFont("comicsans", 50)
        self.selected_tower = None
        self.menu = Tower_menu(85, 240, tower_menu_img)
        self.menu.add_button(quick_archer_img, "quick_archer", 500)
        self.menu.add_button(powerful_archer_img, "powerful_archer", 600)
        self.menu.add_button(range_support_img, "range_support", 1000)
        self.menu.add_button(attack_support_img, "attack_support", 1000)
        self.moving_object = None

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(200)
            #Generates enemies
            if time.time() - self.timer >= 6:
                self.timer = time.time()
                self.enemies.append(random.choice([Knight(), Swordsman(), Battleaxe()]))

            pos = pygame.mouse.get_pos()
            
            #See if object is being moved
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Check for moving object plus mouse down
                    if self.moving_object:

                        if self.moving_object.name in attack_tower_names:
                            self.attack_towers.append(self.moving_objects)
                        elif self.moving_object.name in support_tower_names:
                            self.support_towers.append(self.moving_objects)

                        self.moving_object.moving = False
                        self.moving_object = None
                        
                    else:
                        #Check to see if tower menu icons have been clicked on
                        tower_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if tower_menu_button:
                            print(tower_menu_button)
                        
                        #Check to see if a tower is selected
                        button_clicked = None
                        if self.selected_tower:
                            button_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if button_clicked:
                                if button_clicked == "Upgrade":
                                    cost = self.selected_tower.menu.get_item_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()

                        if not(button_clicked):
                            for tower in self.towers:
                                if tower.click(pos[0],pos[1]):
                                    tower.selected = True
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False

                            for tower in self.support_towers:
                                if tower.click(pos[0],pos[1]):
                                    tower.selected = True
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False
                            
                    

            #Deleting enemies off the screen
            to_del = []
            for enemy in self.enemies:
                if enemy.x > 1130:
                    to_del.append(enemy)

            for d in to_del:
                self.lives -= 1
                self.enemies.remove(d)

            #Loop through towers
            for tower in self.towers:
                self.money += tower.attack(self.enemies)

            #Loop through support towers
            for tower in self.support_towers:
                tower.support(self.towers)

            if self.lives <= 0:
                print("You lose")
                run = False


            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))

        #Towers
        for towers in self.towers:
            towers.draw(self.win)

        #Support towers
        for towers in self.support_towers:
            towers.draw(self.win)

        #Enemies
        for enemy in self.enemies:
            enemy.draw(self.win)

        #Objects being purchased
        if self.moving_object:
            self.moving_object.draw(self.win)

        #Menu
        self.menu.draw(self.win)

        #Game stats
        life = pygame.transform.scale(lives_img,(28,28))
        for x in range(self.lives):
            self.win.blit(life, (10 + life.get_width()*x, 10))

        currency_text = self.font.render(str(self.money), 1, (0, 0, 0))
        money = pygame.transform.scale(star_img, (40, 40))

        self.win.blit(currency_text, (12 + money.get_width(), 55))
        self.win.blit(money, (10, 50))
        
        pygame.display.update()

    def add_tower(self, name):
        name_list = ["quick_archer", "powerful_archer", "range_support", "attack_support"]
        object_list = [QuickArcherTower(), PowerfulArcherTower(), DamageTower(), RangeTower()]
        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "Not valid name")

        

star_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","star.png")), (50, 50))

class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))



class Tower_menu_button(Button):
    def __init__(self, x, y, img, name, cost):
        super().__init__(x, y, img, name)
        self.cost = cost



class Menu:
    def __init__(self,tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.background = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_button(self, img, name):
        self.items += 1
        button_x = ((self.x - self.background.get_width()/2) - 5) + 10
        button_y = (self.y - 140) + 10
        self.buttons.append(Button(button_x, button_y, img, name))

    def get_item_cost(self):
        return self.item_cost[self.tower.level - 1]

    def draw(self, win):
        win.blit(self.background, ((self.x - self.background.get_width()/2) - 5, self.y - 140))
        for item in self.buttons:
            item.draw(win)
            win.blit(star_img, (item.x + item.width + 5, item.y - 9))
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star_img.get_height() - 8))
    
    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X, Y):
                return button.name

        return None



class Tower_menu(Menu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.background = img
        self.font = pygame.font.SysFont("comicsans", 25)

    def add_button(self, img, name, cost):
        self.items += 1
        button_x = self.x - 70
        button_y = self.y - 95 + (self.items - 1)*110
        self.buttons.append(Tower_menu_button(button_x, button_y, img, name, cost))

    def draw(self, win):
        win.blit(self.background, ((self.x - self.background.get_width()/2) - 5, self.y - 140))
        for item in self.buttons:
            item.draw(win)
            win.blit(star_img, (item.x + item.width + 5, item.y + 5))
            text = self.font.render(str(item.cost), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star_img.get_height() + 5))
    



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
        length = 25
        move_by = length // self.max_health
        health_bar = move_by * self.health

        pygame.draw.rect(win, (255,0,0), (self.x - 5, self.y - 55, length, 10), 0)
        pygame.draw.rect(win, (0,255,0), (self.x - 5, self.y - 55, health_bar, 10), 0)

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


    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False



Knight_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    Knight_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy4", "4_enemies_1_run_0" + add_str + ".png")), (64, 64)))
            
class Knight(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 1
        self.health = self.max_health
        self.imgs = Knight_imgs[:]
        self.name = "knight"
        self.reward = 5
        


Battleaxe_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    Battleaxe_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy7", "7_enemies_1_run_0" + add_str + ".png")), (64, 64)))
    
class Battleaxe(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 5
        self.health = self.max_health
        self.imgs = Battleaxe_imgs[:]
        self.name = "battleaxe"
        self.reward = 15
        


Swordsman_imgs = []

for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    Swordsman_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy10", "10_enemies_1_run_0" + add_str + ".png")), (64, 64)))
    
class Swordsman(Enemy):
    def __init__(self):
        super().__init__()
        self.max_health = 3
        self.health = self.max_health
        self.imgs = Swordsman_imgs[:]
        self.name = "swordsman"
        self.reward = 10



menu_background = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface", "menu.png")), (120, 70))
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface", "upgrade.png")), (50, 50))

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
        self.tower_imgs = []
        self.damage = 1
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, "Max lv"])
        self.menu.add_button(upgrade_button, "Upgrade")

    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

        #Drawing menu
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self, win):
        if self.selected:
            #Show range of tower (translucent)
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (255,135,135, 60), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        img = self.tower_imgs[self.level-1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell(self):
        return self.sell_price[self.level-1]

    def upgrade(self):
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def upgrade_cost(self):
        return self.price[self.level-1]

    def move(self, x, y):
        self.x = x
        self.y = y

        
tower_imgs = []
archer_imgs = []
#Archer tower image
for x in range(7,10):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")), (90, 90)))

#Archer character image
for x in range(38,44):
    archer_imgs.append(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")))

class PowerfulArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.in_range = False
        self.left = True
        self.original_damage = self.damage
        self.damage = 1
        self.frequency = 3
        self.width = self.height = 90
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, 5000, "Max lv"])
        self.menu.add_button(upgrade_button, "Upgrade")
        self.moving = False
        self.name = "powerful_archer"

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

        if self.in_range and not self.moving:
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
        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
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
            if self.archer_count == 5:
                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)
                    money = first_enemy.reward
            if first_enemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        return money

tower2_imgs = []
archer2_imgs = []
#Archer tower image
for x in range(10,13):
    tower2_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")), (90, 90)))

#Archer character image
for x in range(51,56):
    archer2_imgs.append(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")))

class QuickArcherTower(PowerfulArcherTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower2_imgs[:]
        self.archer_imgs = archer2_imgs[:]
        self.archer_count = 0
        self.range = 125
        self.in_range = False
        self.left = True
        self.damage = 1
        self.frequency = 6
        self.original_damage = self.damage
        self.menu = Menu(self, self.x, self.y, menu_background, [2500, 6000, "Max lv"])
        self.menu.add_button(upgrade_button, "Upgrade")
        self.name = "quick_archer"


RangeTower_imgs = []
for x in range(4,6):
    RangeTower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/SupportTowers", str(x) + ".png")), (80,80)))

class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 125
        self.original_range = self.range
        self.effect = [0.1, 0.2, 0.3]
        self.tower_imgs = RangeTower_imgs[:]
        self.width = self.height = 80
        self.name = "range_object"

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def support(self, towers):
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if distance <= self.range + tower.width//2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level - 1])


DamageTower_imgs = []
for x in range(7,9):
    DamageTower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/SupportTowers", str(x) + ".png")), (80,80)))
    
class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 125
        self.effect = [0.2, 0.4, 0.5]
        self.tower_imgs = DamageTower_imgs[:]
        self.name = "damage_object"

    def support(self, towers):
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if distance <= self.range + tower.width//2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level - 1])

        

g = Game()
g.run()
