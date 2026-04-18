import pygame
import sys
from ball import Ball

# Инициализация
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

WHITE = (255, 255, 255)

# Создаем шар
ball = Ball(WIDTH//2, HEIGHT//2)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move("up", WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move("down", WIDTH, HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move("left", WIDTH, HEIGHT)
            elif event.key == pygame.K_RIGHT:
                ball.move("right", WIDTH, HEIGHT)
    
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()