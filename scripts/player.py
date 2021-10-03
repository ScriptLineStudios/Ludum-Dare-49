import pygame, math
import random as rd

class particle():
    def __init__(self):
        pass

class trail():
    def __init__(self,color):
        self.color = color
        self.poses = [[[300,0],[330,0]]]

        self.speed = 4

    def draw(self,display):
        index = 0
        for pos in self.poses:
            pos[1][1] -= self.speed
            pos[0][1] -= self.speed
            pygame.draw.line(display,self.color,pos[0],self.poses[index+1][0],width=3)
            pygame.draw.line(display,self.color,pos[1],self.poses[index+1][1],width=3)
            if index < len(self.poses)-2:
                index += 1
            if pos[0][1] < -100:
                self.poses.pop(self.poses.index(pos))
class Player():
    def __init__(self,pos):#xVelocity was never used here:)
        self.pos = pos

        self.angle = 0

        self.trl = trail((170,170,170))
        self.addTrailTimer = 6

        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        self.addAng = 0
        self.addTimer = 0
        self.add = False

    def draw(self,display,mp, game_over):
        if not game_over:
            #movement#
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
            #movement#
            self.angle += self.addAng
            self.addX = math.cos(math.radians(self.angle+90))*5


            self.pos[0] += self.addX

            #addTrail#
            if self.addTrailTimer >= 6:
                self.trl.poses.append([[self.rect.center[0]-math.cos(math.radians(self.angle-90))*30+math.cos(math.radians(self.angle))*9,self.rect.center[1]+math.sin(math.radians(self.angle-90))*30],[self.rect.center[0]-math.cos(math.radians(self.angle-90))*30-math.cos(math.radians(self.angle))*9,self.rect.center[1]+math.sin(math.radians(self.angle-90))*30]])

                self.addTrailTimer = 0
            else:
                self.addTrailTimer += 1

            #print(mp[0], self.pos[0])
            self.trl.draw(display)
            '''if mp[0] > self.pos[0]:
                self.image = pygame.transform.scale(self.image, (64,64))
            elif mp[0] < self.pos[0]:
                self.image = pygame.transform.scale(pygame.transform.flip(self.image, True, False), (64,64))'''
            transformedImg = pygame.transform.rotate(pygame.transform.scale(self.image, (64,64)),self.angle)
            self.rect = transformedImg.get_rect()
            self.rect.topleft = self.pos

            display.blit(transformedImg,self.pos)

        #pygame.draw.circle(display,(255,0,0),[self.rect.center[0]-math.cos(math.radians(self.angle-90))*30+math.cos(math.radians(self.angle))*7,self.rect.center[1]+math.sin(math.radians(self.angle-90))*30],radius=3)
        #pygame.draw.circle(display,(255,0,0),[self.rect.center[0]-math.cos(math.radians(self.angle-90))*30-math.cos(math.radians(self.angle))*7,self.rect.center[1]+math.sin(math.radians(self.angle-90))*30],radius=3)
class rain():
    def __init__(self):
        pass
