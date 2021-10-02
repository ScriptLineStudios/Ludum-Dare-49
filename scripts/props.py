#I don't know *flushed*

class obstacle():
    def __init__(self,image,pos,downSpeed):
        self.pos = pos
        self.image = image

        self.downSpeed = downSpeed
        
        self.rect = self.image.get_rect()

    def draw(self,display):
        display.blit(self.image,self.pos)
        #pygame.draw.rect(display,(255,0,0),self.rect)
        self.pos[1] -= self.downSpeed
        self.rect.topleft = self.pos
