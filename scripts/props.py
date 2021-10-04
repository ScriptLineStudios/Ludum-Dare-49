import pygame
import framework

class Obstacle():
    def __init__(self,pos,image,downSpeed):
        self.pos = pos
        self.image = image

        self.downSpeed = downSpeed

        self.rect = self.image.get_rect()

        self.lifetime = 255

    def draw(self,display):
        self.lifetime -= 1
        display.blit(pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4)),(self.pos[0], self.pos[1]))
        self.pos[1] -= self.downSpeed
        self.rect.topleft = self.pos

class Deer:
    def __init__(self, x, y, down_speed):
        self.x = x
        self.y = y
        self.down_speed = down_speed
        self.images = [pygame.image.load("assets/deers-sheet1.png"), pygame.image.load("assets/deers-sheet2.png"), pygame.image.load("assets/deers-sheet3.png"),
        pygame.image.load("assets/deers-sheet4.png")]
        self.animation_index = 0
        self.dir = 0
        if self.x == 700:
            self.dir = -4
        elif self.x == -300:
            self.dir = 4
        self.rect = None

    def draw(self, display):
        self.rect = (self.x, self.y, self.images[self.animation_index//15].get_width()*4, self.images[self.animation_index//15].get_height()*4)
        self.animation_index = framework.animate(self.images, self.animation_index, 15)
        if self.dir == -4:
            display.blit(pygame.transform.scale(self.images[self.animation_index//15], (self.images[self.animation_index//15].get_width()*4, self.images[self.animation_index//15].get_height()*4)),(self.x, self.y))
        elif self.dir == 4:
            display.blit(pygame.transform.scale(pygame.transform.flip(self.images[self.animation_index//15], True, False), (self.images[self.animation_index//15].get_width()*4, self.images[self.animation_index//15].get_height()*4)),(self.x, self.y))
        self.y -= self.down_speed
        self.x += self.dir
