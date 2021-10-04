import pygame,sys
from pygame.locals import *
pygame.init()

SCRSIZE = (600, 700)
FPS = 60
CAPTION = "Unstable Steep"

display = pygame.display.set_mode((600,700))
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()

in_menu = True

pygame.mixer.music.load("assets/Menu.mp3")
pygame.mixer.music.play(-1)

class button():
    def __init__(self,pos,font,text,color,function):
        self.pos = pos

        self.color = color

        self.font = font
        self.fontRender = font.render(text,False,color)
        self.rect = self.fontRender.get_rect(topleft=self.pos)

        self.halfLen = self.rect.width//2

        self.hovered = False
        self.addLen = 0
        self.addSpeed = 3

        self.function = function

    def draw(self,display,mp):
        display.blit(self.fontRender,self.pos)

        if self.rect.collidepoint(mp):
            self.hovered = True
        else:
            self.hovered = False

        if self.addLen > 0:
            pygame.draw.line(display,self.color,[self.rect.bottomleft[0],self.rect.bottomleft[1]+7],[self.rect.bottomleft[0]+self.addLen,self.rect.bottomleft[1]+7],width=4)
            pygame.draw.line(display,self.color,[self.rect.bottomright[0],self.rect.bottomright[1]+7],[self.rect.bottomright[0]-self.addLen,self.rect.bottomright[1]+7],width=4)

        if self.addLen < self.halfLen and self.hovered == True:
            self.addSpeed += 0.3
            self.addLen += self.addSpeed

        if self.hovered == False:
            self.addSpeed = 0

            if self.addLen > 0:
                self.addLen -= 3

    def start_func(self):
        self.function()

class settings():
    def __init__(self):
        self.opened = False

    def draw(self,display):
        display.fill((255,255,255))#self.settingsMenu

    def openFunc(self):
        self.opened = True

class Credits():
    def __init__(self):
        pass

def hello():
    print('hello')

def exitFunc():
    pygame.quit()
    sys.exit()

def load_font(font_name, font_size):#borrowed from framework;)
    return pygame.font.Font(font_name, font_size)

class main_menu():
    def __init__(self):#235,57,120  235,222,80 33,194,235
        self.BackGround = pygame.image.load('scripts/menu_test.png').convert()
        self.opened = True

        self.settingsMenu = settings()
        self.credits = Credits()

        self.CircleRadius = 350
        self.minusSpeed = 5

        font80 = load_font("assets/dpcomic.ttf",80)

        self.in_menu = True

        self.buttons = [
            button([25,250],font80,'Play',(33,194,235),self.openFunc),
            button([25,350],font80,'Settings',(30,132,158),hello),
            button([25,450],font80,'Credits',(96,235,67),hello),
            button([25,550],font80,'Exit',(235,57,120),exitFunc)
            ]

    def draw(self,display,mp):
        display.blit(self.BackGround,(0,0))
        if self.opened == True:
            for but in self.buttons:
                but.draw(display,mp)
        if self.CircleRadius > 0:
            pygame.draw.circle(display,(0,0,0),[display.get_width()//2,display.get_height()//2],self.CircleRadius)
            self.CircleRadius -= self.minusSpeed
            self.minusSpeed += 0.1
    def IfCollide(self):
        for button in self.buttons:
            if button.hovered == True:
                button.start_func()

    def openFunc(self):
        self.in_menu = False
menu = main_menu()
while menu.in_menu:
    display.fill((255,255,255))

    mp = pygame.mouse.get_pos()
    menu.draw(display,mp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                menu.IfCollide()


    clock.tick(FPS)
    pygame.display.update()
