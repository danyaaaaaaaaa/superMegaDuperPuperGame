import pygame
import os
import time
import random

pygame.init()

#Размер окна
win_width = 1000
win_height = 700

#Фпс
FPS = 30

#Наход файлов в папке с исходником
PATH = ""   #os.path.dirname(__file__) + os.sep

#Количество уфо и скоко пропустид
ufos = 8
misedufo = 0
hited = 0



#Скрипт по созданию изображений
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageS, width, height, x,y, speed):
        super().__init__()
        self.image = pygame.image.load(imageS)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def show(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))
#Основной класс ГГ
class Hero(GameSprite):
    def wasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] == True:
            self.rect.x -= 14
        if keys[pygame.K_RIGHT] == True:
            self.rect.x += 14
        if keys[pygame.K_SPACE] == True:
            BULLETS.add(Bullet(PATH + 'bullet.png', 10, 50, self.rect.centerx, self.rect.y, 5))
#Клас врагов(уфо)
class UFO(GameSprite):
    def update(self):
        global misedufo, misedtext, hited
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0 - ufo_height
            self.rect.x = random.randint(0, win_width-ufo_width)
            misedufo += 1
            misedtext = label.render("Улетели: " + str(misedufo), True, (255, 255, 255))
            

            
#Класс пули
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

#Создание окна
wind = pygame.display.set_mode((win_width, win_height))
back = GameSprite(PATH + 'galaxy.jpg', win_width, win_height, 0,0, 0)

#Создание героя
hero = Hero(PATH + 'rocket.png', 50, 70, win_width/2, win_height-70, 50)

#Создание надписи пропущеныъ НЛО
label = pygame.font.Font(None, 50)

misedtext = label.render("Улетели: 0", True, (255, 255, 255))
pasted = label.render("Сбито: 0", True, (255, 255, 255))

#Размеры НЛО
ufo_width = 100
ufo_height = 50

#Списки УФО и Пуль
UFO_LIST = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()

i = 0
while i < ufos:
    UFO_LIST.add(UFO(PATH + 'ufo.png', ufo_width, ufo_height, random.randint(0, win_width-ufo_width), 0 - ufo_height, random.randint(2, 6)))
    i += 1

game = True

clock = pygame.time.Clock()

while game == True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game = False
    clock.tick(FPS)

    hero.wasd()
    #for ufo in UFO_LIST:
    #   ufo.move()
    UFO_LIST.update()
    BULLETS.update()

    collide = pygame.sprite.groupcollide(UFO_LIST, BULLETS, True, True)
    for hit in collide:
        print("hit")
        hited += 1
        pasted = label.render("Сбито: " + str(misedufo), True, (255, 255, 255))
        UFO_LIST.add(UFO(PATH + 'ufo.png', ufo_width, ufo_height, random.randint(0, win_width-ufo_width), 0 - ufo_height, random.randint(2, 6)))



    if hited == 10:
        game = False
    
    if misedufo == 15:
        game = False

    back.show()   
    hero.show()

    #for ufo in UFO_LIST:
        #ufo.show()
    UFO_LIST.draw(wind)
    BULLETS.draw(wind)

    
    wind.blit(misedtext, (10, 10))
    wind.blit(pasted, (10, 40))
    pygame.display.update()
