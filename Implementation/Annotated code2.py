import pygame
import os
import math
import time
import random

#Initialise font module
pygame.font.init()
#Load heart image for lives counter
lives_img = pygame.image.load(os.path.join("Game_images/GameInterface","heart.png"))
#Load tower menu background
tower_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","menu2.png")), (150, 500))
#Tower menu icon images
range_support_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","range_support.png")), (75, 75))
attack_support_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","attack_support.png")), (75, 75))
powerful_archer_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","powerful_archer.png")), (75, 75))
quick_archer_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","quick_archer.png")), (75, 75))
#Global names for type of tower
support_tower_names = ["range_object", "damage_object"]
attack_tower_names = ["powerful_archer", "quick_archer"]

class Game_menu:
    #Constructor
    def __init__(self):
        #Window size
        self.width = 1100
        self.height = 700
        #Initialise a window or screen for display
        self.win = pygame.display.set_mode((self.width, self.height))
        #Menu image
        self.game_menu_img = pygame.image.load(os.path.join("Game_images","GameMenu2.png"))
        self.game_menu_img = pygame.transform.scale(self.game_menu_img, (self.width, self.height))

    #Menu run method
    def run(self):
        intro = True
        clock = pygame.time.Clock()
        while intro:
            #This is the amount of frames that should pass per second
            clock.tick(15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    intro = False
                #When button is pressed it goes to game
                if event.type == pygame.KEYDOWN:
                    g = Game()
                    g.run()
                    intro = False
                if intro:
                    #Call draw method
                    self.draw()
        pygame.quit()

    #Method to draw any objects into the actual game
    def draw(self):
        #Draw menu background
        self.win.blit(self.game_menu_img, (0,0))
        pygame.display.update()

class Game:
    #Constructor
    def __init__(self):
        #Window size
        self.width = 1100
        self.height = 700
        #Initialise a window or screen for display
        self.win = pygame.display.set_mode((self.width, self.height))
        #Empty lists for enemies and towers
        self.enemies = []
        self.towers = []
        self.support_towers = []
        #Amount of lives and money that the player has
        self.lives = 10
        self.money = 10000
        #Image and scaling for the game background 
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        #Timer for spawning enemies
        self.timer = time.time()
        #Font for writing
        self.font = pygame.font.SysFont("comicsans", 50)
        #What tower has been selected
        self.selected_tower = None
        #Instantiate tower menu
        self.menu = Tower_menu(85, 240, tower_menu_img)
        #Instantiation of tower menu buttons
        self.menu.add_button(quick_archer_img, "quick_archer", 500)
        self.menu.add_button(powerful_archer_img, "powerful_archer", 600)
        self.menu.add_button(range_support_img, "range_support", 1000)
        self.menu.add_button(attack_support_img, "attack_support", 1000)
        #Determines if a tower is being placed
        self.moving_object = None

    #Method that holds and executes the actual game loop
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            #This is the amount of frames that should pass per second
            clock.tick(180)
            
            #When time interval is greater than 6
            if time.time() - self.timer >= 6:
                #Set equal for next interval
                self.timer = time.time()
                #Spawn random choice of enemy 
                self.enemies.append(random.choice([Knight(), Clubman(), Swordsman(), Battleaxe(), Axeman()]))

            #Gets mouse position
            pos = pygame.mouse.get_pos()

            #See if object is being moved
            if self.moving_object:
                #Object follows the mouse position
                self.moving_object.move(pos[0], pos[1])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                #If mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Check for moving object plus mouse down
                    if self.moving_object:
                        #If moving object is an attack tower
                        if self.moving_object.name in attack_tower_names:
                            #Add to attack tower list
                            self.towers.append(self.moving_object)
                        #If moving object is a support tower
                        elif self.moving_object.name in support_tower_names:
                            #Add to support tower list
                            self.support_towers.append(self.moving_object)
                        #Reset once complete
                        self.moving_object.moving = False
                        self.moving_object = None
                        
                    else:
                        #Check to see if tower menu icons have been clicked on
                        tower_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if tower_menu_button:
                            #If player has enough money for tower
                            if self.money >= self.menu.get_item_cost(tower_menu_button):
                                #Deduct tower cost from money
                                self.money -= self.menu.get_item_cost(tower_menu_button)
                                #Add tower
                                self.add_tower(tower_menu_button)
                        
                        #Check to see if a tower is selected
                        button_clicked = None
                        if self.selected_tower:
                            #Button pressed
                            button_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if button_clicked:
                                #If upgrade button is clicked
                                if button_clicked == "Upgrade":
                                    #Get cost of tower upgrade
                                    cost = self.selected_tower.menu.get_item_cost()
                                    #If player has enough money to cover cost
                                    if self.money >= cost:
                                        #Take cost away from player money
                                        self.money -= cost
                                        #Upgrade tower
                                        self.selected_tower.upgrade()

                        if not(button_clicked):
                            #Run through tower list
                            for tower in self.towers:
                                #Check if attacking tower has been clicked on
                                if tower.click(pos[0],pos[1]):
                                    tower.selected = True
                                    #Assign selected tower
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False
                            #Run through support tower list
                            for tower in self.support_towers:
                                #Check if any have been clicked on
                                if tower.click(pos[0],pos[1]):
                                    tower.selected = True
                                    #Assign selected tower
                                    self.selected_tower = tower
                                else:
                                    tower.selected = False

            #Deleting enemies off the screen
            to_del = []
            for enemy in self.enemies:
                #If enemy is off the screen
                if enemy.x > 1130:
                    #Add to the delete list
                    to_del.append(enemy)

            #Remove all enemies in delete list
            for d in to_del:
                #Player loses a life
                self.lives -= 1
                #Enemy is then removed
                self.enemies.remove(d)

            #Loop through towers
            for tower in self.towers:
                self.money += tower.attack(self.enemies)

            #Loop through support towers
            for tower in self.support_towers:
                tower.support(self.towers)

            #Once player has no lives
            if self.lives <= 0:
                print("You lose")
                #Game is terminated
                run = False

            self.draw()
            

        pygame.quit()

    #Method to draw any objects into the actual game
    def draw(self):
        self.win.blit(self.background, (0,0))

        #draw all towers in tower list
        for towers in self.towers:
            towers.draw(self.win)

        #Draw towers in tower support list
        for towers in self.support_towers:
            towers.draw(self.win)

        #draw enemies
        for enemy in self.enemies:
            enemy.draw(self.win)

        #Objects being purchased
        if self.moving_object:
            self.moving_object.draw(self.win)
        
        #Draw menu
        self.menu.draw(self.win)

        #Draw game stats
        #Assign image to attribute with scaling
        live = pygame.transform.scale(lives_img,(28,28))
        #Draws a heart for each life
        for x in range(self.lives):
            self.win.blit(live, (10 + live.get_width()*x, 10))

        #Display of currency
        currency_text = self.font.render(str(self.money), 1, (0, 0, 0))
        money = pygame.transform.scale(star_img, (40, 40))

        self.win.blit(currency_text, (12 + money.get_width(), 55))
        self.win.blit(money, (10, 50))

        pygame.display.update()

    #Method for adding towers
    def add_tower(self, name):
        #Coordinates of mouse position
        x, y = pygame.mouse.get_pos()
        #List of tower names
        name_list = ["quick_archer", "powerful_archer", "range_support", "attack_support"]
        #List of tower objects
        object_list = [CrossBowTower(x,y), PowerfulArcherTower(x,y), RangeTower(x,y), DamageTower(x,y)]
        #Tests block
        try:
            #Assigns relevant tower according to name given in argument
            obj = object_list[name_list.index(name)]
            #Obj is now moving object with mouse
            self.moving_object = obj
            obj.moving = True
        #If it does not work
        except Exception as e:
            print(str(e) + "Not valid name")

#Load star image for in game currency
star_img = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface","star.png")), (50, 50))

#Class for button
class Button:
    #Constructor
    def __init__(self, menu, img, name):
        #Name of button
        self.name = name
        #Button image
        self.img = img
        #Coordinates of menu 
        self.x = menu.x - 55
        self.y = menu.y - 130
        self.menu = menu
        #Width of image
        self.width = self.img.get_width()
        #Height of image
        self.height = self.img.get_height()

    #Click method
    def click(self, X, Y):
        #If in designated hit zone
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    #Method for drawing button
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    #Method to update position of button
    def update(self):
        self.x = self.menu.x - 55
        self.y = self.menu.y - 130

#Class for tower menu button
#Subclass of button
class Tower_menu_button(Button):
    #Constructor
    def __init__(self, x, y, img, name, cost):
        #Name
        self.name = name
        #Image
        self.img = img
        #Coordinates for position
        self.x = x
        self.y = y
        #Dimensions
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        #Cost of tower
        self.cost = cost

#Menu class
class Menu:
    #Constructor
    def __init__(self,tower, x, y, img, item_cost):
        #x coordinate
        self.x = x
        #y coordinate
        self.y = y
        #Menu width
        self.width = img.get_width()
        #Menu height
        self.height = img.get_height()
        #Cost of item
        self.item_cost = item_cost
        #Amount of items
        self.items = 0
        #List for menu buttons
        self.buttons = []
        #Menu background image
        self.background = img
        #Font for text
        self.font = pygame.font.SysFont("comicsans", 25)
        #Tower
        self.tower = tower

    #Method for adding buttons to menu
    def add_button(self, img, name):
        #Add an extra item
        self.items += 1
        #Add new object to the list
        self.buttons.append(Button(self, img, name))

    #Gets cost of item
    def get_item_cost(self):
        return self.item_cost[self.tower.level - 1]

    #Draw method
    def draw(self, win):
        #Draws menu background
        win.blit(self.background, ((self.x - self.background.get_width()/2) - 5, self.y - 140))
        #Draws all menu items
        for item in self.buttons:
            item.draw(win)
            win.blit(star_img, (item.x + item.width + 5, item.y - 9))
            #Assigns item cost
            text = self.font.render(str(self.item_cost[self.tower.level - 1]), 1, (255,255,255))
            #Draws item cost under star icon
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star_img.get_height() - 8))

    #Click method
    def get_clicked(self, X, Y):
        #Determines if button has been clicked
        for button in self.buttons:
            if button.click(X, Y):
                #If it has gives name of button
                return button.name
        return None

    #Menu update
    def update(self):
        #Runs through the buttons
        for button in self.buttons:
            #Calls button update method
            button.update()
    
#Menu subclass
class Tower_menu(Menu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        #Width of image
        self.width = img.get_width()
        #Height of image
        self.height = img.get_height()
        #List for tower menu buttons
        self.buttons = []
        #Number of items
        self.items = 0
        #tower menu background image
        self.background = img
        #Desired font for price dislay 
        self.font = pygame.font.SysFont("comicsans", 25)

    #Method for adding buttons
    def add_button(self, img, name, cost):
        #Each time button is created an item is added
        self.items += 1
        #Spacing for button
        button_x = self.x - 70
        button_y = self.y - 95 + (self.items - 1)*110
        #Instantiating tower menu button
        self.buttons.append(Tower_menu_button(button_x, button_y, img, name, cost))

    #Method for getting tower cost
    def get_item_cost(self, name):
        #Run through button list
        for button in self.buttons:
            #Check if name of button matches input
            if button.name == name:
                #Return cost
                return button.cost
        #Finished            
        return -1

    #Method for drawing menu
    def draw(self, win):
        #Background
        win.blit(self.background, ((self.x - self.background.get_width()/2) - 5, self.y - 140))
        #Draws button for each item in tower menu
        for item in self.buttons:
            item.draw(win)
            win.blit(star_img, (item.x + item.width + 5, item.y + 5))
            text = self.font.render(str(item.cost), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star_img.get_height() + 5))

#Enemy superclass
class Enemy:
    #Constructor
    def __init__(self):
        self.width = 64
        self.height = 64
        #Position in the animation loop
        self.animation_count = 0
        #Enemy health
        self.health = 1
        #Coordinates of points on the path
        self.path = [(1110, 142), (1078, 142), (485, 144), (418, 162), (394, 197), (379, 240), (380, 282), (450, 328), (480, 340), (540, 350), (570, 390), (600, 448), (620, 500), (620, 560), (620, 561), (622, 562), (667, 563), (724, 563), (1026, 563), (1095, 563), (1150,563)]
        self.x = self.path[0][0]
        self.y = self.path [0][1]
        self.img = None
        #Position in the path list
        self.path_pos = 0
        #Amount of times enemy has moved
        self.move_count = 0
        #Distance enemy has moved
        self.distance = 0
        #list that holds images for enemy animation 
        self.imgs = []
        #Boolean that determines if the image has been flipped or not
        self.flipped = False
        #Maximum amount of health enemy can have
        self.max_health = 0

    def draw(self, win):
        #Position in the images list for animation
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1

        #reset count when animation gets to the end of images
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        #Draws position of enemy which goes through centre of the image
        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 20))
        #Draws health bar above enemy
        self.draw_health_bar(win)
        self.move()

    #Method to draw health bar above enemy
    def draw_health_bar(self, win):
        #Length of bar
        length = 25
        #Distance to move the current health bar
        move_by = length / self.max_health
        health_bar = move_by * self.health

        #Draws max health bar above enemy
        pygame.draw.rect(win, (255,0,0), (self.x - 5, self.y - 55, length, 10), 0)
        #Draws current health bar above enemy
        pygame.draw.rect(win, (0,255,0), (self.x - 5, self.y - 55, health_bar, 10), 0)

    #Collide method that will be used later to detect any attacks on enemy
    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    #Method to move enemy
    def move(self):
        #Sets current points coordinates
        x1, y1 = self.path[self.path_pos]
        #Sets next points coordinates
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1120, 582)
        else:
            x2, y2 = self.path[self.path_pos+1]

        #Calculates direction and magnitude
        direction = (x2-x1, y2-y1)
        length = math.sqrt((direction[0])**2 + (direction[1])**2)
        #Then makes direction into a unit vector
        direction = (direction[0]/length, direction[1]/length)

        #Flips the image if it's moving in the positive x direction so it looks like it's walking in the correct direction
        if direction[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)
        #Flips the image back once it has flipped already
        elif direction[0] > 0 and self.flipped == True:
            self.flipped = False
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        #Calculates distance that will be moved
        move_x, move_y = ((self.x + direction[0]), (self.y + direction[1]))

        #Moves enemy to desired location
        self.x = move_x
        self.y = move_y

        #Next point in list
        #Moving right
        if direction[0] >= 0:
            #Moving down
            if direction[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            #Moving up
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        #Moving left
        else:
            #Moving down
            if direction[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            #Moving up
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
                    
    #Method for if enemy is attacked
    def hit(self, damage):
        #Amount of damage tower deals
        #is deducted from enemy health
        self.health -= damage
        if self.health <= 0:
            return True
        return False


#List for knight images
knight_imgs = []
#Preload animation loop for knight movement
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    knight_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy4", "4_enemies_1_run_0" + add_str + ".png")), (50, 50)))
            
#Enemy subclass
class Knight(Enemy):
    #Inherits attributes from enemy superclass
    def __init__(self):
        super().__init__()
        #Load knight animation slicing list
        self.imgs = knight_imgs[:]
        #Maximum amount of health
        self.max_health = 1
        #Current amount of health
        self.health = self.max_health
        self.name = "knight"
        #Amount rewarded for killing
        self.reward = 5


#List for battleaxe images
battleaxe_imgs = []
#Preload animation loop for battleaxe movement
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    battleaxe_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy7", "7_enemies_1_run_0" + add_str + ".png")), (65, 65)))

#Enemy subclass
class Battleaxe(Enemy):
    #Inherits attributes from enemy superclass
    def __init__(self):
        super().__init__()
        #Load battleaxe animation slicing list
        self.imgs = battleaxe_imgs[:]
        #Maximum amount of health
        self.max_health = 5
        #Current amount of health
        self.health = self.max_health
        self.name = "battleaxe"
        #Amount rewarded for killing
        self.reward = 25


#List for swordsman images
swordsman_imgs = []
#Preload animation loop for swordsman movement
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    swordsman_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy10", "10_enemies_1_run_0" + add_str + ".png")), (70, 70)))
    
#Enemy subclass
class Swordsman(Enemy):
    #Inherits attributes from enemy superclass
    def __init__(self):
        super().__init__()
        #Load swordsman animation slicing list
        self.imgs = swordsman_imgs[:]
        #Maximum amount of health
        self.max_health = 3
        #Current amount of health
        self.health = self.max_health
        self.name = "swordsman"
        #Amount rewarded for killing
        self.reward = 15

#List for axeman images
Axeman_imgs = []
#Preload animation loop for axeman movement
for x in range(10):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    Axeman_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy1", "2_enemies_1_RUN_0" + add_str + ".png")), (64, 64)))

#Enemy subclass
class Axeman(Enemy):
    def __init__(self):
        super().__init__()
        #Maximum amount of health
        self.max_health = 10
        #Current amount of health
        self.health = self.max_health
        self.imgs = Axeman_imgs[:]
        self.name = "axeman"
        #Amount rewarded for killing
        self.reward = 50

#List for clubman images
Clubman_imgs = []
#Preload animation loop for clubman movement
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    Clubman_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/Enemy2", "3_enemies_1_run_0" + add_str + ".png")), (55, 55)))

#Enemy subclass
class Clubman(Enemy):
    def __init__(self):
        super().__init__()
        #Maximum amount of health
        self.max_health = 2
        #Current amount of health
        self.health = self.max_health
        self.imgs = Clubman_imgs[:]
        self.name = "clubman"
        #Amount rewarded for killing
        self.reward = 10

#Preload menu img
menu_background = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface", "menu.png")), (120, 70))
#Preload upgrade img
upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("Game_images/GameInterface", "upgrade.png")), (50, 50))

#Tower superclass
class Tower:
    #Tower constructor
    def __init__(self, x, y):
        #Position of tower
        self.x = x
        self.y = y
        #Size of tower
        self.width = 0
        self.height = 0
        #Sell and buy price lists
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        #Tower level
        self.level = 1
        #Determines if tower is selected or not
        self.selected = False
        #Different images for tower
        self.tower_imgs = []
        #Amount of damage tower deals
        self.damage = 1
        #instantiate Menu
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, "Max lv"])
        #Call on add button method to create button object
        self.menu.add_button(upgrade_button, "Upgrade")

    #Method for drawing tower
    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

        #Drawing menu
        if self.selected:
            self.menu.draw(win)

    #Method for drawing tower radius
    def draw_radius(self, win):
        #Show selected towers radius
        if self.selected:
            #Show range of tower (translucent)
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (255,135,135, 60), (self.range, self.range), self.range, 0)
            win.blit(surface, (self.x - self.range, self.y - self.range))
    
    #Returns true if the tower is clicked on 
    def click(self, X, Y):
        #Tower image
        img = self.tower_imgs[self.level-1]
        #Uses image width and height for hit box
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False
    
    #Returns the sell price of tower
    def sell(self):
        return self.sell_price[self.level-1]

    #Method to upgrade tower
    def upgrade(self):
        if self.level < len(self.tower_imgs):
            #Level increases by 1
            self.level += 1
            #Damage increases by 1
            self.damage += 1

    #Returns the cost of the upgrade for that level
    def upgrade_cost(self):
        return self.price[self.level-1]

    #Allows you to move tower to desired x and y 
    def move(self, x, y):
        self.x = x
        self.y = y
        #Update position of menu
        self.menu.x = x
        self.menu.y = y
        #Menu update
        self.menu.update()

#List for tower images
tower_imgs = []
#list for archer animation
archer_imgs = []
#Archer tower image
for x in range(7,10):
    tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")), (90, 90)))

#Archer character image
for x in range(38,44):
    archer_imgs.append(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")))

#Tower subclass
class PowerfulArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        #Tower name
        self.name = "powerful_archer"
        #Instantiate menu
        self.menu = Menu(self, self.x, self.y, menu_background, [2000, 5000, "Max lv"])
        self.menu.add_button(upgrade_button, "Upgrade")
        #List of tower images
        self.tower_imgs = tower_imgs[:]
        #List of archer images
        self.archer_imgs = archer_imgs[:]
        #Tracks position of archer animation in list
        self.archer_count = 0
        #Range of tower
        self.range = 200
        #Determines if enemy is in range
        self.in_range = False
        #Original range of the tower
        self.original_range = self.range
        #Determines if archer is facing left
        self.left = True
        #Amount of damage tower deals
        self.damage = 1
        #Towers original damage
        self.original_damage = self.damage
        #Width and height of tower
        self.width = self.height = 90
        #Determines if tower is moving
        self.moving = False

    #Gets cost of tower upgrade
    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    #Draw method
    def draw(self, win):
        #Inherits draw radius method
        super().draw_radius(win)
        #Inherits draw method from superclass
        super().draw(win)
        #Only animates when enemy is in range or not moving 
        if self.in_range and not self.moving:
            self.archer_count += 1
            #Checks if archer count needs to be reset
            if self.archer_count >= len(self.archer_imgs)*3:
                self.archer_count = 0

        else:
            self.archer_count = 0

        #Selects the archer to draw from desired position in animation
        archer = self.archer_imgs[self.archer_count//3]
        #If archer is facing left
        if self.left == True:
            #When flipped archer tends to right side
            #So add will be used to takeaway 25 from x coordinate
            add = -25
        else:
            #Value to centre archer when facing right
            add = -archer.get_width() + 10
        #Draws archer
        #Adds the add value to the archers x coordinate
        win.blit(archer, ((self.x + add), (self.y - archer.get_height() - 25)))

    #Changes range of tower depending on the radius
    def change_range(self, r):
        self.range = r
    
    #Attacks enemies in enemy list
    #Enemies must be in tower range
    def attack(self, enemies):
        #Money earnt for attack
        money = 0
        self.in_range = False
        #List for closest enemy
        enemy_closest = []
        #Goes through the enemy list
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            #Calculates distance of tower from enemy
            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            #If distance is less than range it can attack
            if distance < self.range:
                #Now true
                self.in_range = True
                #Adds enemy to list
                enemy_closest.append(enemy)

        #Sorts the enemy closest list
        enemy_closest.sort(key=lambda x: x.x)
        #If there's any enemies in range
        if len(enemy_closest) > 0:
            #Closest enemy is assigned
            first_enemy = enemy_closest[0]
            #If it's the 5th animation
            if self.archer_count == 5:
                #If enemy has no health left
                if first_enemy.hit(self.damage) == True:
                    #Enemy is removed
                    enemies.remove(first_enemy)
                    #Amount earned for killing that enemy
                    money = first_enemy.reward
                    
            #If enemy is on the left of the tower
            if first_enemy.x > self.x and not(self.left):
                self.left = True
                #Flips animation to face left
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            #If enemy is on the right of the tower
            elif self.left and first_enemy.x < self.x:
                self.left = False
                #Flips animation to face right
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)

        #Return amount of money for killing that enemy
        return money

#Cross bow tower image list
tower2_imgs = []
#Archer 2 animation list
archer2_imgs = []
#Archer tower image
for x in range(10,13):
    tower2_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")), (90, 90)))

#Archer character image
for x in range(51,56):
    archer2_imgs.append(pygame.image.load(os.path.join("Game_images/ArcherTowers", str(x) + ".png")))

#Powerful archer tower subclass
#Overrides attributes to be unique
class CrossBowTower(PowerfulArcherTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        #Tower name
        self.name = "quick_archer"
        #Instantiate menu
        self.menu = Menu(self, self.x, self.y, menu_background, [2500, 6000, "Max lv"])
        self.menu.add_button(upgrade_button, "Upgrade")
        #Image lists
        self.tower_imgs = tower2_imgs[:]
        self.archer_imgs = archer2_imgs[:]
        #Archer animation position
        self.archer_count = 0
        #Range of tower
        self.range = 125
        #Determines if enemy is in range
        self.in_range = False
        #Determines if archer is facing left
        self.left = True
        #Amount of damage
        self.damage = 2
        #Towers original damage
        self.original_damage = self.damage

#Load RangeTower images
RangeTower_imgs = []
for x in range(4,6):
    RangeTower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/SupportTowers", str(x) + ".png")), (80,80)))

#Subclass of Tower
class RangeTower(Tower):
    #Constructor
    def __init__(self, x, y):
        super().__init__(x,y)
        #Name of tower
        self.name = "range_object"
        #Range
        self.range = 125
        #Original range
        self.original_range = self.range
        #Effect increase when upgraded
        self.effect = [0.1, 0.2, 0.3]
        #Images
        self.tower_imgs = RangeTower_imgs[:]
        #Width and height
        self.width = self.height = 80

    #Draw method
    def draw(self, win):
        #Use draw radius method from tower
        super().draw_radius(win)
        super().draw(win)

    #Support method
    def support(self, towers):
        #List of towers that are effected by support
        effected = []
        #Gets coordinates of all attacking towers
        for tower in towers:
            x = tower.x
            y = tower.y
            #Works out distance between tower and support tower
            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            #If in range of support tower
            if distance <= self.range + tower.width//2:
                #Attacking tower is added to effected list
                effected.append(tower)
        #Effected towers have range increased depending on level
        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level - 1])

#Load Damage Tower images
DamageTower_imgs = []
for x in range(7,9):
    DamageTower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Game_images/SupportTowers", str(x) + ".png")), (80,80)))

#Subclass of RangeTower
class DamageTower(RangeTower):
    #Constructor
    def __init__(self, x, y):
        super().__init__(x,y)
        #Name of tower
        self.name = "damage_object"
        #Radius
        self.range = 125
        #Effect increase when upgraded
        self.effect = [0.2, 0.4, 0.5]
        #Images
        self.tower_imgs = DamageTower_imgs[:]

    #Support methods
    def support(self, towers):
        #List of towers that are effected by support
        effected = []
        #Gets coordinates of all attacking towers
        for tower in towers:
            x = tower.x
            y = tower.y
            #Works out distance between tower and support tower
            distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            #If in range of support tower
            if distance <= self.range + tower.width//2:
                #Attacking tower is added to effected list
                effected.append(tower)
        #Effected towers have damage increased depending on level
        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level - 1])


#List for audio clips
playlist = []
#Append desired game sound
playlist.append("bensound-epic.mp3")
#Initialise mixer
pygame.mixer.init()
#Pop audio file
pygame.mixer.music.load(playlist.pop())
#Play on repeated loop
pygame.mixer.music.play(-1)
#Executes the run function of the game class
m = Game_menu()
m.run()
