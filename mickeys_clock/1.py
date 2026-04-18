#Create a simple clock application (only with minutes and seconds) which is synchronized with system clock.
# Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: 
#  pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144


import pygame
import datetime
import math

pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
fps = 50
font = pygame.font.SysFont('Verdana', 36)

game = True

yellow = (255, 255, 0)
Radius = 360
clock60 = dict(zip(range(60), range(0, 360, 6)))

images = pygame.image.load("body.PNG")
right_hand = pygame.image.load("right-hand.PNG") #minutes
left_hand = pygame.image.load("left-hand.PNG")   #seconds

main = pygame.transform.scale(images,(600,600))
hand2 = pygame.transform.scale(left_hand, (250 , 70))
hand1 = pygame.transform.scale(right_hand, (160, 80))

main_rect = main.get_rect()

hand1_rect = hand1.get_rect(bottomright = (630, 320))
hand1_rotate = pygame.transform.rotate(hand1, 0)

hand2_rect = hand2.get_rect(bottomleft = (400,380))
hand2_rotate = pygame.transform.rotate(hand2, -8)


def get_clock_pos(clock_dict, clock_hand):
    x = 410 + 300 * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = 410 + 300 * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    

    time = datetime.datetime.now()
    second = time.second
    minute = time.minute
    
    position_minute = get_clock_pos(clock60, minute)
    position_second = get_clock_pos(clock60, second)
    
    screen.fill((0, 50, 0))
    pygame.draw.circle(screen, yellow, (width/2, height/2), 280)
    screen.blit(main, (100, 10))
    
    #action for minutes
    right_angle = math.atan2(position_minute[1] - (hand1_rect[1] + 32), position_minute[0] - hand1_rect[0] + 26)
    hand1_rotated = pygame.transform.rotate(hand1_rotate, 720 - right_angle * 57.29)

    right = (hand1_rect[0] - hand1_rotated.get_rect().width/2, hand1_rect[1] - hand1_rotated.get_rect().height/2) 
    screen.blit(hand1_rotated, right)

    #action for seconds
    left_angle = math.atan2(position_second[1] - (hand2_rect[1] + 32), position_second[0] - (hand2_rect[0] + 26))
    left_hand_rotated = pygame.transform.rotate(hand2_rotate, 360 - left_angle * 57.29)
    
    left_rect = (hand2_rect[0] - left_hand_rotated.get_rect().width/2, hand2_rect[1] - left_hand_rotated.get_rect().height/2)
    screen.blit(left_hand_rotated, left_rect)
    
    time_render = font.render(f"{time:%H:%M:%S}", True, (25, 100, 100), (255, 255, 255))
    screen.blit(time_render, (0, 0))
    pygame.display.update()
    clock.tick(fps)


