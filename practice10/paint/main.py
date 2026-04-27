import pygame

pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Lab 10: 1-Pencil, 2-Rect, 3-Circle, 4-Eraser, R/G/B-Colors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN.fill(WHITE)
current_color = BLACK
tool = 'pencil'
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Құралдарды және түстерді таңдау
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: tool = 'pencil'
            if event.key == pygame.K_2: tool = 'rect'
            if event.key == pygame.K_3: tool = 'circle'
            if event.key == pygame.K_4: tool = 'eraser'
            if event.key == pygame.K_r: current_color = RED
            if event.key == pygame.K_g: current_color = GREEN
            if event.key == pygame.K_b: current_color = BLUE
            if event.key == pygame.K_k: current_color = BLACK

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if tool == 'rect':
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(SCREEN, current_color, (x, y, w, h), 2)
            elif tool == 'circle':
                rad = int(((start_pos[0]-end_pos[0])**2 + (start_pos[1]-end_pos[1])**2)**0.5)
                pygame.draw.circle(SCREEN, current_color, start_pos, rad, 2)
            start_pos = None

        # Үздіксіз сурет салу (қарындаш немесе өшіргіш)
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            if tool == 'pencil':
                pygame.draw.circle(SCREEN, current_color, event.pos, 3)
            elif tool == 'eraser':
                pygame.draw.circle(SCREEN, WHITE, event.pos, 20)

    pygame.display.flip()

pygame.quit()