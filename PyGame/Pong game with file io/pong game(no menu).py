import pygame

def draw_text(surf, text, size, x, y): 
    font = pygame.font.SysFont("comicsansms",20)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
#End function

# -- Global Constants
game_over = False

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
def game_loop(screen):
    score_left = 0
    score_right = 0
    paddle_block_x = 10
    paddle_block_y = display_height//2
    paddle2_block_x = 615
    paddle2_block_y = display_height//2
    paddle2_speed = 7
    paddle2_direction = 0
    speed = 8
    direction = 0
    ball_x_val = 150
    ball_y_val = 200
    ball_x_offset = 3
    ball_y_offset = 3
    computer_speed = 7
    end_count = 0
    highscore = 0
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

        #Making the left paddle move
        paddle_block_y = paddle_block_y + direction * speed


        #Making the right paddle move
        if paddle2_block_y > ball_y_val:
            paddle2_block_y -= computer_speed
        elif paddle2_block_y < ball_y_val:
            paddle2_block_y += computer_speed
        #End if


        #Adding score to the board and restarting ball
        if ball_x_val <= 10:
            score_right += 1
            ball_x_val = display_width // 2
            ball_y_val = display_height // 2
            ball_x_val += ball_x_offset
            ball_y_val += ball_y_offset
            end_count = 0
            ball_x_offset = 3
            ball_y_offset = 3
        elif ball_x_val >= 630:
            score_left += 1
            ball_x_val = display_width // 2
            ball_y_val = display_height // 2
            ball_x_val += ball_x_offset
            ball_y_val += ball_y_offset
            end_count = 0
            ball_x_offset = 3
            ball_y_offset = 3
        #End if

        
        #Making the ball bounce off the wall
        if ball_y_val > 480 - 10 or ball_y_val < 10:
            ball_y_offset *= -1
        #End if
        if ball_x_val > 640 - 10 or ball_x_val < 10:
            ball_x_offset *= -1
        #End if


        #Making the ball collide with the left and right paddle, plus controlling its speed, as well as highscore
        ball_x_val = ball_x_val + ball_x_offset
        ball_y_val = ball_y_val + ball_y_offset
        if ball_x_val < 35 and ball_y_val > paddle_block_y and ball_y_val < paddle_block_y + 60:
            ball_x_offset *= -1
            end_count += 1
            if end_count > 4:
                ball_x_offset += 1
                ball_y_offset += 1
            #End if
            if end_count > highscore:
                highscore = end_count
                f = open("highscore.txt","wt")
                f.write(str(highscore))
                f.close
            #End if
        elif ball_x_val > 605 and ball_y_val > paddle2_block_y and ball_y_val < paddle2_block_y + 60:
            ball_x_offset *= -1
            end_count += 1
            if end_count > 4:
                ball_x_offset += 1
                ball_y_offset += 1
            #End if
            if end_count > highscore:
                highscore = end_count
                f = open("highscore.txt","wt")
                f.write(str(highscore))
                f.close
            #End if
        #End if


        #Update position of the ball
        ball_x_val += ball_x_offset
        ball_y_val += ball_y_offset

            
        # -- Screen background is BLACK
        screen.fill (BLACK)


        # -- Draw here
        pygame.draw.rect(screen, WHITE, (paddle_block_x, paddle_block_y, 15, 60))
        pygame.draw.rect(screen, WHITE, (paddle2_block_x, paddle2_block_y, 15, 60))
        pygame.draw.circle(screen, BLUE, (ball_x_val,ball_y_val),10,2)
        draw_text(screen, 'Highscore: ' + (str(highscore), 18, 20, 10)
        draw_text(screen, (str(score_left) + ' : ' + str(score_right)), 18, display_width / 2, 10)
        

        # -- flip display to reveal new position of objects
        pygame.display.flip()


        # - The clock ticks over
        clock.tick(60)


    #End While - End of game loop
#End function
  
game_loop(screen)
pygame.quit()
#quit()
