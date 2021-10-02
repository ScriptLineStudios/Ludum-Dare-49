import pygame,sys
from pygame.locals import *
pygame.init()

SCRSIZE = (600, 700)
FPS = 60
CAPTION = "Drunk skier"

display = pygame.display.set_mode((600,700))
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()

class button():
    def __init__(self,pos,font,text,color):
        self.pos = pos

        self.color = color

        self.font = font
        self.fontRender = font.render(text,False,color)
        self.rect = self.fontRender.get_rect(topleft=self.pos)

        self.halfLen = self.rect.width//2

        self.hovered = False
        self.addLen = 0
        self.addSpeed = 1

    def draw(self,display,mp):
        display.blit(self.fontRender,self.pos)

        if self.rect.collidepoint(mp):
            self.hovered = True
        else:
            self.hovered = False

        if self.addLen > 0:
            pygame.draw.line(display,self.color,[self.rect.bottomleft[0],self.rect.bottomleft[1]+10],[self.rect.bottomleft[0]+self.addLen,self.rect.bottomleft[1]+10],width=4)
            pygame.draw.line(display,self.color,[self.rect.bottomright[0],self.rect.bottomright[1]+10],[self.rect.bottomright[0]-self.addLen,self.rect.bottomright[1]+10],width=4)

        if self.addLen < self.halfLen and self.hovered == True:
            self.addSpeed += 0.15
            self.addLen += self.addSpeed

        if self.hovered == False:
            self.addSpeed = 0

            if self.addLen > 0:
                self.addLen -= 3
                
class main_menu():
    def __init__(self):
        self.button_1 = button([100,100],pygame.font.Font(None,50),'Ludum Dare 49',(0,0,0))

    def draw(self,display,mp):
        self.button_1.draw(display,mp)

menu = main_menu()
while True:
    display.fill((255,255,255))

    mp = pygame.mouse.get_pos()
    menu.draw(display,mp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    clock.tick(FPS)
    pygame.display.update()
