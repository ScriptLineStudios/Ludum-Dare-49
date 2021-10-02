import pygame
from pygame.locals import *
from scripts.player import Player
import sys
#import noise
import math
import random
pygame.init()

WINDOW_SIZE = (600, 700)
FPS = 60
CAPTION = "Unstable Steep"

display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
#player
player = Player([WINDOW_SIZE[0]//2,125],2)


#generation
points = []
y = 0

def generate_terrain():
    global y
    for x in range(8):
        points.append([random.randrange(200, 400), y])
        y += 200

scroll_y = 2
time_until_next_generation = 0
while True:
    display.fill((255,255,255))
    if time_until_next_generation == 0:
        generate_terrain()
        time_until_next_generation = 80
    else:
        time_until_next_generation -= 1

    mp = pygame.mouse.get_pos()


    player.draw(display,mp)


    for index, point in enumerate(points):
        if points[index][1] > -200:
            points[index][1] -= scroll_y
            if index != len(points)-1:
                pygame.draw.line(display, (0,0,0), (points[index][0]+8, points[index][1]+8), (points[index+1][0]+8, points[index+1][1]+8), width=1)
            pygame.draw.rect(display, (0,0,0), (point[0], point[1], 16, 16))
        else:
            points.remove(point)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()

    clock.tick(FPS)
    pygame.display.update()
