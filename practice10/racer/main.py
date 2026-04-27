import pygame, sys
import random, time

pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Lab 10")

FPS = 60
clock = pygame.time.Clock()

# Түстер мен Қаріптер
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("Verdana", 20)

# Ойын айнымалылары
SPEED = 5
SCORE = 0
COINS = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Сурет болмаса жай қызыл квадрат жасаймыз
        self.image = pygame.Surface((40, 70))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Сарғыш түсті тиын
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)

    def reset(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.reset()

# Спрайттарды дайындау
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(WHITE)
    
    # Ұпай мен Тиынды көрсету
    coin_text = font.render(f"Coins: {COINS}", True, BLACK)
    SCREEN.blit(coin_text, (WIDTH-120, 10))

    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)
        entity.move()

    # Тиын жинауды тексеру
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        C1.reset()

    # Соқтығысу (Game Over)
    if pygame.sprite.spritecollideany(P1, enemies):
        SCREEN.fill(RED)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)