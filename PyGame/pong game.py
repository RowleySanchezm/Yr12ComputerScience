import pygame

game_over = False

def text_objects_red(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()
#End function

def text_objects_black(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
#End function

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
        #End if
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects_black(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)
    #End if
#End function
    
def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #End if
        #Next event
        screen.fill(BLACK)
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects_red("Welcome To Pong", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button("GO!",100,400,100,50,GREEN,BRIGHT_GREEN,game_loop)
        button("Quit",430,400,100,50,RED,BRIGHT_RED,game_over)

        pygame.display.update()
        clock.tick(15)
    #End while
#End function

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (200,0,0)
GREEN = (0,200,0)
BRIGHT_RED = (255,0,0)
BRIGHT_GREEN = (0,255,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
display_width = 640
display_height = 480
size = (display_width,display_height)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong game")




### -- Game Loop
def game_loop():
    paddle_block_x = 10
    paddle_block_y = size[1]//2
    speed = 8
    direction = 0
    ball_x_val = 150
    ball_y_val = 200
    ball_x_offset = 3
    ball_y_offset = 3
    global game_over
    while not game_over:
        
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = - 1
                elif event.key == pygame.K_DOWN:
                    direction = 1
                #End If
            elif event.type == pygame.KEYUP:
                direction = 0
            #End If
        #Next event

                
        # -- Game logic goes after this comment

        #making the paddle move
        paddle_block_y = paddle_block_y + direction * speed
        ball_x_val = ball_x_val + ball_x_offset
        ball_y_val = ball_y_val + ball_y_offset

        #Making the ball bounce off the wall
        if ball_y_val > 480 - 10 or ball_y_val < 10:
            ball_y_offset *= -1
        #End if 
        if ball_x_val > 640 - 10 or ball_x_val < 10:
            ball_x_offset *= -1
        #End if

        #Making the ball collide with the left paddle
        if ball_x_val < 35 and ball_y_val > paddle_block_y and ball_y_val < paddle_block_y + 60:
            ball_x_offset *= -1
        #End if

        #Update position of the ball
        ball_x_val += ball_x_offset
        ball_y_val += ball_y_offset
            
        # -- Screen background is BLACK
        screen.fill (BLACK)

        # -- Draw here

        pygame.draw.rect(screen, WHITE, (paddle_block_x, paddle_block_y, 15, 60))
        pygame.draw.circle(screen, BLUE, (ball_x_val,ball_y_val),10,2)

        # -- flip display to reveal new position of objects
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)

    #End While - End of game loop

        
game_intro()
game_loop()
pygame.quit()
quit()
