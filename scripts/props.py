#I don't know *flushed*
import pygame

class Obstacle():
    def __init__(self,pos,image,downSpeed):
        self.pos = pos
        self.image = image

        self.downSpeed = downSpeed

        #self.rect = self.image.get_rect()

    def draw(self,display):
        display.blit(self.image,(self.pos[0], self.pos[1]))
        self.pos[1] -= self.downSpeed

class YAwareGroup(pygame.sprite.Group):
    def by_y(self, spr):
        return spr.pos.y

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sorted(sprites, key=self.by_y):
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []
