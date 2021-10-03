import pygame

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
