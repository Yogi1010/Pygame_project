import pygame, time, sys, random
from pygame.locals import *

pygame.init()
class Road(pygame.sprite.Sprite):
    image=None
    def __init__(self,y):
        pygame.sprite.Sprite.__init__(self)
        if Road.image is None:
            Road.image=pygame.image.load('road.jpg')
        self.image=Road.image
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y= y+car_height

#coins
class Ball(pygame.sprite.Sprite):
    image=None
    #it derives from the "Sprite" class in pygame
    def __init__(self,color,width,height):

        #Call the Parent(Sprite) class constructor
        pygame.sprite.Sprite.__init__(self)
        if Ball.image is None:
            Ball.image=pygame.image.load('shoe.jpg')
        self.image=Ball.image
        #update the coordinates of the image
        self.rect=self.image.get_rect()
#Barack Obama
class obama(pygame.sprite.Sprite):
    image=None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if obama.image is None:
            obama.image=pygame.image.load('Obama.jpg')
        self.image=obama.image
        #update the coordinates of the image
        self.rect=self.image.get_rect()

    def locate(self, x, y):
        self.rect.topleft = [x, y]


#Vladimir Putin
class put(pygame.sprite.Sprite):
        image = None

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            if put.image is None:
                put.image = pygame.image.load('putin.jpg')
            self.image = put.image
            # update the coordinates of the image
            self.rect = self.image.get_rect()
        def locate(self,x,y):
            self.rect.topleft = [x, y]

#George Bush
class Bush(pygame.sprite.Sprite):
            image = None

            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                if Bush.image is None:
                    Bush.image = pygame.image.load('Bush.jpg')
                self.image = Bush.image
                # update the coordinates of the image
                self.rect = self.image.get_rect()

            def locate(self, x, y):
                self.rect.topleft = [x, y]


class Bullets(Ball):
    def update(self):
        self.rect.y -= 3


#constants
display_width=1366
display_height=768
car_width=156
car_height=265
x = display_width * 0.4
y = display_height * 0.5

#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
RED          = (155,   0,   0)
GREEN        = (  0, 155,   0)
BLUE         = (  0,   0, 155)
LIGHT_BLUE   = (  0,   0, 255)
LIGHT_GREEN  = (  0, 155,   0)
LIGHT_RED    = (155,   0,   0)
O_BLUE       = (0  , 162, 232)

DISPLAYSURF = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('OBAMA SHOOTING!!!')
clock = pygame.time.Clock()

modiImg=pygame.image.load('Modi.jpg')

bush=Bush()
obm=obama()
putin=put()
road=Road(y-10)
all_sprite_list=pygame.sprite.Group()
bullet_list=pygame.sprite.Group()
sprite_list=pygame.sprite.Group()


all_sprite_list.add(bush)
all_sprite_list.add(obm)
all_sprite_list.add(putin)

sprite_list.add(bush)
sprite_list.add(obm)
sprite_list.add(putin)


def quitgame():
    pygame.quit()


def modi(x, y):
    DISPLAYSURF.blit(modiImg,(x, y))


def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    textSurf, textRect= text_objects(text, largeText)
    textRect.center= ((display_width/2),(display_height/2))
    DISPLAYSURF.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display("Game Over!!!")


#button function
def button(msg, x, y, w, h, i, a,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and  y + h > mouse[1] > y :
        pygame.draw.rect(DISPLAYSURF, a, (x, y, w, h))
        if click[0] == 1 and action!=None:
            action()
    else:
        pygame.draw.rect(DISPLAYSURF, i, (x, y, w, h))
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects(msg,smalltext)
    textRect.center = ((x+w/2),(y+h/2))
    DISPLAYSURF.blit(textSurf, textRect)


# start screen interface
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects("OBAMA SHOOTING!!!", largeText)
        textRect.center = ((display_width / 2), (display_height / 2))
        DISPLAYSURF.blit(textSurf, textRect)
        pygame.display.update()
        button("PLAY" , 150, 450, 100, 50, BLUE, LIGHT_BLUE,game_loop)
        button("QUIT", 1150, 450, 100, 50, BLUE, LIGHT_BLUE,quitgame)
        pygame.display.update()
        clock.tick(10)

#game playing interface
def game_loop():
    bush = Bush()
    obm = obama()
    putin = put()
    all_sprite_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    sprite_list = pygame.sprite.Group()

    all_sprite_list.add(bush)
    all_sprite_list.add(obm)
    all_sprite_list.add(putin)
    all_sprite_list.add(road)

    sprite_list.add(bush)
    sprite_list.add(obm)
    sprite_list.add(putin)

    x = display_width * 0.4
    y = display_height * 0.5
    xrout=-600
    yrout=-600
    gameExit = False
    #Frames per second
    FPS = 40
    x_change = 0
    y_change = 0
    monst_starty=20
    monst_width=50
    monst_height=50
    monst_count=random.randrange(1,2)
    dodgedo=0
    dodgedp=0
    dodgedb=0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


          #  pygame.draw.rect(DISPLAYSURF,BLACK,[y+car_height,display_width,display_height-y-car_height])
           # pygame.display.update()
            #all_sprite_list.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -15
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 15
                elif event.key == pygame.K_SPACE:
                    monst_startx = random.randrange(0, display_width)
                    xin = random.randrange(1, 4)
                    if xin == 1:
                        obm.locate(monst_startx, monst_starty)
                        putin.locate(xrout, yrout)
                        bush.locate(xrout, yrout)
                    elif xin == 2:
                        putin.locate(monst_startx, monst_starty)
                        bush.locate(xrout, yrout)
                        obm.locate(xrout, yrout)
                    elif xin == 3:
                        bush.locate(monst_startx, monst_starty)
                        obm.locate(xrout, yrout)
                        putin.locate(xrout, yrout)

                    bullet = Bullets(BLACK, 4, 10)
                    bullet.rect.x = x
                    bullet.rect.y = y
                    all_sprite_list.add(bullet)
                    bullet_list.add(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                    x_change= 0

        x += x_change
        #car should not cross the boundaries
        if x>display_width-car_width or x<0:
            crash()

        if y>display_height-car_height or y<0:
            crash()

        DISPLAYSURF.fill(O_BLUE)
        modi(x,y)
        all_sprite_list.update()
        bullet_list.update()
        for bullet in bullet_list:
            hit_list = pygame.sprite.spritecollide(bullet, sprite_list, True)
            for obm in hit_list:
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
                dodgedo +=1
                pygame.mixer.music.load('slap.mp3')
                pygame.mixer.music.play(1)

            for bush in hit_list:
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
                dodgedb += 1
                pygame.mixer.music.load('slap.mp3')
                pygame.mixer.music.play(1)

            for putin in hit_list:
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
                dodgedp += 1
                pygame.mixer.music.load('slap.mp3')
                pygame.mixer.music.play(1)

            if bullet.rect.y < -10 :
                bullet_list.remove(bullet)
                all_sprite_list.remove(bullet)
                pygame.mixer.music.load('beep9.mp3')
                pygame.mixer.music.play(1)

            if dodgedo ==1:
                message_display("OBAMA DEAD!!!")
                crash()
                break
            elif dodgedb ==1:
                message_display("BUSH DEAD!!!")
                crash()
                break
            elif dodgedp ==1:
                message_display("PUTIN DEAD!!!")
                crash()
                break



        all_sprite_list.draw(DISPLAYSURF)
        pygame.display.update()

        clock.tick(FPS)


img = pygame.image.load('water.jpg')
DISPLAYSURF.blit(img, (0, 0))
pygame.display.update()
game_intro()
game_loop()
pygame.quit()