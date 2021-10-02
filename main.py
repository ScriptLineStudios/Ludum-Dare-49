import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.props import Obstacle, YAwareGroup
import framework
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

tree_img = pygame.image.load("assets/tree.png")
shadow_img = pygame.image.load("assets/shadow.png")
rock_img = pygame.image.load("assets/rock.png")

clock = pygame.time.Clock()

#player
player = Player([WINDOW_SIZE[0]//2,125],2)


#generation
points = []
decorations = []
y = 0

obstacles = []
obstacle_rects = []

spawn_y = 0

#text
font = framework.load_font("assets/dpcomic.ttf", 64)


distance = 0

def generate_terrain():
    global y
    prev_x = 0
    prev_y = 0
    for x in range(32):
        x = random.randrange(250, 350)
        points.append([x, y])
        for _ in range(5):
            rand_x = random.randrange(-300, 300)
            rand_y = random.randrange(-200,200)

            img = random.choice([tree_img, rock_img, tree_img])
            obstacle_rects.append(pygame.Rect(x-20+rand_x+img.get_width()/2, y+rand_y+img.get_height()-40, 32, 40))
            obstacles.append(Obstacle([x-8+rand_x, y+rand_y],img, 4))
        y += 400




scroll_y = 4
time_until_next_generation = 0
distance_timer = 0
game_over = False

while True:
    '''if player.rect.x-300 > 60: ---> This was going to be the code for making the player wobble more as you more further out
        player.addTimer = 60
    elif player.rect.x-300 < -200:
        player.addTimer = 60
    else:
        player.addTimer = 30'''
    if distance_timer == 0 and not game_over:
        distance += 1
        distance_timer = 60
    else:
        distance_timer -= 1
    display.fill((246,246,246))
    if time_until_next_generation == 0:
        generate_terrain()
        time_until_next_generation = 160
    else:
        time_until_next_generation -= 1


    mp = pygame.mouse.get_pos()



    for index, point in enumerate(points):
        if points[index][1] > -600:
            points[index][1] -= scroll_y
            if index != len(points)-1:
                pygame.draw.line(display, (196,233,242), (points[index][0]+1, points[index][1]+8), (points[index+1][0]+1, points[index+1][1]+8), width=70)
            #pygame.draw.rect(display, (0,0,0), (point[0], point[1], 2, 2))
        else:
            points.remove(point)

    player.draw(display,mp)

    #pygame.draw.rect(display, (0,0,0), pygame.Rect(player.rect.x+10, player.rect.y+10, player.rect.width-20, player.rect.height-20), 1)


    for obstacle in obstacles:
        display.blit(shadow_img, (obstacle.pos[0]+obstacle.image.get_width()/2-30, obstacle.pos[1]+obstacle.image.get_height()-55))
        obstacle.draw(display)
    for rect in obstacle_rects:
        rect[1] -= scroll_y
        if rect.colliderect(pygame.Rect(player.rect.x+10, player.rect.y+10, player.rect.width-20, player.rect.height-20)):
            game_over = True
        #pygame.draw.rect(display, (0,0,0), rect, 1)



    if game_over:
        framework.render_text(display, "GAME OVER!", font, True, (0,0,0), (140,250))
        framework.render_text(display, "DISTANCE: " + str(distance) + "m", font, True, (0,0,0), (140,300))
    else:
        distance_text = "Distance: " + str(distance) + "m"
        framework.render_text(display, distance_text, font, True, (0,0,0), (25,25))

    framework.handle_particles(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()

    clock.tick(FPS)
    pygame.display.update()
