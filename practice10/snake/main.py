import pygame
import random
import time

pygame.init()

# Экран өлшемдері
WIDTH, HEIGHT = 600, 400
CELL = 20
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Түстер
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 10
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.score = 0
        self.level = 1

    def move(self):
        head = self.body[0].copy()
        if self.direction == "RIGHT": head[0] += CELL
        if self.direction == "LEFT": head[0] -= CELL
        if self.direction == "UP": head[1] -= CELL
        if self.direction == "DOWN": head[1] += CELL
        self.body.insert(0, head)

    def check_collision(self):
        head = self.body[0]
        # Қабырғаға соғылу
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        # Өз денесіне соғылу
        if head in self.body[1:]:
            return True
        return False

# Жаңа тамақ орнын табу (жыланның үстіне түспеуі керек)
def get_random_food_pos(snake_body):
    while True:
        pos = [random.randrange(0, WIDTH // CELL) * CELL, 
               random.randrange(0, HEIGHT // CELL) * CELL]
        if pos not in snake_body:
            return pos

snake = Snake()
food_pos = get_random_food_pos(snake.body)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN": snake.direction = "UP"
            if event.key == pygame.K_DOWN and snake.direction != "UP": snake.direction = "DOWN"
            if event.key == pygame.K_LEFT and snake.direction != "RIGHT": snake.direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake.direction != "LEFT": snake.direction = "RIGHT"

    snake.move()

    # Тамақ жеу
    if snake.body[0] == food_pos:
        snake.score += 1
        food_pos = get_random_food_pos(snake.body)
        # Деңгейді көтеру және жылдамдықты арттыру
        if snake.score % 3 == 0:
            snake.level += 1
            FPS += 2 
    else:
        snake.body.pop()

    if snake.check_collision():
        running = False

    SCREEN.fill(BLACK)
    for pos in snake.body:
        pygame.draw.rect(SCREEN, GREEN, (pos[0], pos[1], CELL, CELL))
    pygame.draw.rect(SCREEN, RED, (food_pos[0], food_pos[1], CELL, CELL))
    
    pygame.display.set_caption(f"Score: {snake.score} Level: {snake.level}")
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()