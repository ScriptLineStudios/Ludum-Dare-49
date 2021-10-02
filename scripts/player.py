import pygame, math
import random as rd
class Player():
    def __init__(self,pos,xVelocity):
        self.pos = pos
        self.xVelocity = xVelocity
        self.angle = 0

        self.unstableDir = {'left':False,'right':False}

        self.trail = []

        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.addAng = 0
        self.addTimer = 0
        self.add = False

    def draw(self,display,mp):
        if rd.randint(0,100) == 10:
            self.addTimer = 30
            self.add = rd.choice([False,True])


        if self.addTimer <= 0:
            if self.addAng > 0:
                self.addAng -= 0.5
            elif self.addAng < 0:
                self.addAng += 0.5

        self.angle = math.degrees(math.atan2(self.rect.center[0]-mp[0],self.rect.center[1]-mp[1]))
        if self.addTimer > 0:
            self.addTimer -= 1
            if self.add == False:
                self.addAng += 1
            else:
                self.addAng -= 1
        self.angle += self.addAng
        self.addX = math.cos(math.radians(self.angle+90))*5
        self.pos[0] += self.addX
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        display.blit(pygame.transform.rotate(self.image,self.angle),self.pos)

class trail():
    def __init__(self,liveTime,color):
        self.liveTime = 100

        self.color = color
        self.poses = []

    def draw(self,display):
        pygame.draw.line(display,self.color,self.poses[0],self.poses[1],width = 5)
