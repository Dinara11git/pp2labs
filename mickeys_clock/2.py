import pygame
import os

pygame.init()

path = r"C:\Users\Hp\Desktop\pp2labs\Lab7\music"
music = os.listdir(path)
print(music)

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Music player")

pygame.mixer.music.load(os.path.join(path, music[0]))

now = 0
paused = False
playing = False

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_n:
                now = (now + 1) % len(music)
                pygame.mixer.music.load(os.path.join(path, music[now]))
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_p:
                now = (now - 1) % len(music)
                pygame.mixer.music.load(os.path.join(path, music[now]))
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                paused = False

    pygame.display.update()
