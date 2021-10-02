import pygame, math

class Player():
    def __init__(self,pos,xVelocity):
        self.pos = pos
        self.xVelocity = xVelocity
        self.angle = 0

        self.unstableDir = {'left':False,'right':False}

        self.trail = []

        self.image = pygame.image.load('assets/player.png')

    def draw(self,display,mp):
        self.angle = math.atan2(self.pos[0]-mp[0],self.pos[1]-mp[1])        
        self.multiplyX = self.angle
        self.addX = math.cos(math.radians(self.angle))*self.multiplyX

        self.pos[0] += self.addX
        
        display.blit(pygame.transform.rotate(self.image,math.degrees(self.angle)),self.pos)

class trail():
    def __init__(self,liveTime,color):
        self.liveTime = 100

        self.color = color
        self.poses = []

    def draw(self,display):
        pygame.draw.line(display,self.color,self.poses[0],self.poses[1],width = 5)
