import pygame

pygame.init()

Width = 800
Height = 600

screen = pygame.display.set_mode((Width, Height))

White = (255, 255, 255)
Red = (255, 0, 0)
Action = True

fps = 60
clock = pygame.time.Clock()

x = 50
y = 50

while Action:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Action = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y >= 25:
        y -= 20
    elif key[pygame.K_DOWN] and y <= 575:
        y += 20
    elif key[pygame.K_RIGHT] and x <= 775:
        x += 20
    elif key[pygame.K_LEFT] and x >= 25:
        x -= 20

    screen.fill(White)
    pygame.draw.circle(screen, Red, (x, y), 25)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
