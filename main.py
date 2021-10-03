import pygame
from pygame.locals import *
from scripts.player import Player
from scripts.props import Obstacle
import framework
import sys
#import noise
import math
import random

pygame.init()

FPS = 60
CAPTION = "Unstable Steep"


WINDOW_SIZE = (700,800)
screen = pygame.display.set_mode(WINDOW_SIZE,0,0)
display = pygame.Surface((700/2,800/2))
pygame.display.set_caption(CAPTION)

tree_imgs = [
    pygame.image.load("assets/tree1.png"),
    pygame.image.load("assets/tree2.png"),
    pygame.image.load("assets/tree3.png"),
    pygame.image.load("assets/tree4.png")
    ]
shadow_img = pygame.image.load("assets/shadow.png")
shadow_img.set_alpha(100)
rock_img = pygame.image.load("assets/rock.png")

clock = pygame.time.Clock()

#player
player = Player([WINDOW_SIZE[0]//4,50])


#generation
points = []
decorations = []
y = 0

obstacles = []
obstacle_rects = []

spawn_y = 0

#text
font = framework.load_font("assets/dpcomic.ttf", 32)

pygame.mixer.music.load("assets/Gameplay.ogg")
pygame.mixer.music.play(-1)

distance = 0

difficulty_index = 0
difficulty_levels = [2, 2, 3, 3, 4, 4, 5, 5]
difficulty_changes = [500, 1000, 1500, 2000, 2500]

def generate_terrain():
    global y
    prev_x = 0
    prev_y = 0
    for x in range(1):
        x = random.randrange(150, 175)
        points.append([x, y])
        '''for _ in range(100):
            rand_x = random.randrange(-25, 25)
            rand_y = random.randrange(-800, 800)
            decorations.append([x+rand_x, y+rand_y])'''

        for _ in range(difficulty_levels[difficulty_index]):
            rand_x = random.randrange(-300, 300)
            rand_y = random.randrange(-200,200)


            img = random.choice([tree_imgs[0], rock_img])

            obstacle_rects.append(pygame.Rect(x+rand_x+5+img.get_width()/2, (y+rand_y+img.get_height()*4)-img.get_height()/2, img.get_width(), img.get_height()))
            obstacles.append(Obstacle([x-8+rand_x, y+rand_y],img, 4))
        y += 100

'''pLeft = []
pRight = []
for point in points:
    pLeft.append([point[0]-500,point[1]])
    pRight.append([point[0]+500,point[1]])'''


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
    fps = str(int(clock.get_fps()))

    if distance_timer == 0 and not game_over:
        distance += 1
        distance_timer = 1
    else:
        distance_timer -= 1
    display.fill((246,246,246))
    if time_until_next_generation == 0:
        generate_terrain()

        time_until_next_generation = 25
    else:
        time_until_next_generation -= 1

    mx, my = pygame.mouse.get_pos()
    mp = (mx/2, my/2)

    print(len(points))

    if distance in difficulty_changes:
        difficulty_index += 1


    #restart_button.draw(display, mp)

    for point in decorations:
        point[1] -= scroll_y
        if point[1] < -100:
            decorations.remove(point)
        pygame.draw.rect(display, (196,233,242), (point[0], point[1], 4,4))




    for index, point in enumerate(points):
        if points[index][1] > -200:
            points[index][1] -= scroll_y
            if index != len(points)-1:
                pygame.draw.line(display, (196,233,242), (points[index][0]+8, points[index][1]+8), (points[index+1][0]+8, points[index+1][1]+8), width=50)
            #pygame.draw.rect(display, (0,0,0), (point[0], point[1], 16, 16))
        else:
            points.remove(point)


    '''pLeft = [[0,WINDOW_SIZE[1]],[0,0]]
    pRight = [[WINDOW_SIZE[0],WINDOW_SIZE[1]],[WINDOW_SIZE[0],0]]
    for point in points:
        pLeft.append([point[0]-250,point[1]])
    for point in points:
        pRight.append([point[0]+250,point[1]])

    pygame.draw.polygon(display,(196,233,242),pLeft)
    pygame.draw.polygon(display,(196,233,242),pRight)'''

    player.draw(display,mp,game_over)

    framework.render_text(display, fps, font, True, (0,0,0), (50,75))

    for index, obstacle in enumerate(obstacles):
        if obstacle.pos[1] < -100:
            obstacles.remove(obstacle)
            obstacle_rects.remove(obstacle_rects[index])

        display.blit(shadow_img, (obstacle.pos[0]+obstacle.image.get_width(), obstacle.pos[1]+obstacle.image.get_height()*4-20))
        obstacle.draw(display)
    for rect in obstacle_rects:

        rect[1] -= scroll_y
        if rect.colliderect(pygame.Rect(player.rect.x+20, player.rect.y+32, player.rect.width/4, player.rect.height/4)):
            game_over = True

    framework.particle_burst()

    if game_over:
        framework.render_text(display, "GAME OVER!", font, True, (0,0,0), (107,100))
        framework.render_text(display, "DISTANCE: " + str(distance) + "m", font, True, (0,0,0), (90,150))
        framework.render_text(display, "PRESS E TO RESTART", font, True, (0,0,0), (65,200))
    else:
        distance_text = "Distance: " + str(distance) + "m"
        framework.render_text(display, distance_text, font, True, (0,0,0), (25,25))

    framework.handle_particles(display)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if game_over:
                    difficulty_index = 0
                    distance_timer = 0
                    distance = 0
                    player.pos = [WINDOW_SIZE[0]//4,50]
                    game_over = False

    clock.tick(FPS)
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
