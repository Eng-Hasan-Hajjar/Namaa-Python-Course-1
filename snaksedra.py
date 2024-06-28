import pygame
import time
import random

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIN_WIDTH = 500
WIN_HEIGHT = 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

clock = pygame.time.Clock()

def show_message(message, color):
    font_style = pygame.font.SysFont("arial", 35)
    message_style = font_style.render(message, True, color)
    window.blit(message_style, (WIN_WIDTH / 3, WIN_HEIGHT / 3))

def draw_snake(snake_list):
    for t in snake_list:
        pygame.draw.rect(window, GREEN, (t[0], t[1], SNAKE_BLOCK, SNAKE_BLOCK))

def display_score(score, color):
    font_style = pygame.font.SysFont("verdana", 25)
    score_style = font_style.render("Score: " + str(score), True, color)
    window.blit(score_style, (10, 10))
    pygame.draw.line(window, color, (0, 50), (WIN_WIDTH, 50))

def game_loop():  
    X = 250
    Y = 200
    X_change = 0
    Y_change = 0   
    
    foodx = random.randrange(0, WIN_WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
    foody = random.randrange(50, WIN_HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)
    
    snake_length = 1
    snake_list = []

    game_close = False
    game_over = False
    while not game_close:
        while game_over:
            window.fill(BLACK)
            show_message("Game Over", RED)
            pygame.display.update()
            time.sleep(3)
            game_close = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    X_change = SNAKE_BLOCK
                    Y_change = 0
                elif event.key == pygame.K_LEFT:
                    X_change = -SNAKE_BLOCK
                    Y_change = 0   
                elif event.key == pygame.K_DOWN:
                    Y_change = SNAKE_BLOCK
                    X_change = 0   
                elif event.key == pygame.K_UP:
                    Y_change = -SNAKE_BLOCK
                    X_change = 0   

        X += X_change##  X =X+ X_change
        Y += Y_change

        if X < 0 or X >= WIN_WIDTH or Y < 50 or Y >= WIN_HEIGHT:
            game_over = True

        window.fill(BLACK)
        pygame.draw.rect(window, BLUE, (foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK))
        
        snake_head = (X, Y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
        
        draw_snake(snake_list)
        display_score(snake_length - 1, WHITE)
        pygame.display.update() 

        if X == foodx and Y == foody:
            snake_length += 1
            foodx = random.randrange(0, WIN_WIDTH - SNAKE_BLOCK, SNAKE_BLOCK)
            foody = random.randrange(50, WIN_HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)

        clock.tick(SNAKE_SPEED)           

    pygame.quit()

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Snake Game")
game_loop()