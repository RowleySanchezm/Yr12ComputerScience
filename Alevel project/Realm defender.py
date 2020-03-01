import pygame
import os

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("Game_images","background1.png"))
        self.clicks = []

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(pos)
                    

            self.draw()
            

        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)
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
        self.path = []
        self.img = None

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

        pass

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True


g = Game()
g.run()
