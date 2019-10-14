import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Manages how fast screen refreshes

clock = pygame.time.Clock()


# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong game")

game_over = False
paddle_block_x = 10
paddle_block_y = size[1]//2
speed = 8
direction = 0
ball_x_val = 150
ball_y_val = 200
ball_x_offset = 3
ball_y_offset = 3

### -- Game Loop
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
    if ball_x_val > 640 - 10 or ball_x_val < 10:
        ball_x_offset *= -1

    #Making the ball collide with the paddle
    if ball_x_val < 35 and ball_y_val > paddle_block_y and ball_y_val < paddle_block_y + 60:
        ball_x_offset *= -1

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

pygame.quit()
