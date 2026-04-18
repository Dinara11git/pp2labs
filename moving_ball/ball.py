import pygame

class Ball:
    def __init__(self, x, y, radius=25, color=(255, 0, 0), speed=20):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self, direction, width, height):
        if direction == "up" and self.y - self.radius - self.speed >= 0:
            self.y -= self.speed
        elif direction == "down" and self.y + self.radius + self.speed <= height:
            self.y += self.speed
        elif direction == "left" and self.x - self.radius - self.speed >= 0:
            self.x -= self.speed
        elif direction == "right" and self.x + self.radius + self.speed <= width:
            self.x += self.speed