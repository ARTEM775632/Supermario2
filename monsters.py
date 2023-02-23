#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import os

#Объявляем переменные
WIN_WIDTH = 2500 #Ширина создаваемого окна
WIN_HEIGHT = 1400 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"
screen = display.set_mode(DISPLAY) # Создаем окошко
#перенесено из файла

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32

OGRE_WIDTH = 90
OGRE_HEIGHT = 90

MONSTER_COLOR = "#2110FF"
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами


ANIMATION_MONSTERHORYSONTAL = [('%s/monsters/fire1.png' % ICON_DIR),
                      ('%s/monsters/fire2.png' % ICON_DIR )]
ogre_images = [] # массив из картинок огров в 4 стороны в трёх состояниях норм-0, атака-1, умер-2
        # ogre_images[0][0] - налево живой
        # ogre_images[0][1] - налево атака
        # ogre_images[0][2] - налево умер
        # ogre_images[1][0] - вниз живой
        # ogre_images[1][1] - вниз атака
        # ogre_images[1][2] - вниз умер
init()

ogr_image_pack = ['monsters/orge_left32.png', 'monsters/orge_down32.png', 'monsters/orge_right32.png', 'monsters/orge_up32.png']



for image_name in ogr_image_pack:
    temp = image.load(image_name).convert_alpha()
    temp.set_colorkey((255, 255, 255))
    i=[]
    i.append(temp.subsurface(0, 0, 32, 32))
    i.append(temp.subsurface(32, 0, 32, 32))
    i.append(temp.subsurface(64, 0, 32, 32))
    ogre_images.append(i)

class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft,maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.startX = x # начальные координаты
        self.startY = y
        self.maxLengthLeft = maxLengthLeft # максимальное расстояние, которое может пройти в одну сторону
        self.maxLengthUp= maxLengthUp # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.xvel = left # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = up # скорость движения по вертикали, 0 - не двигается
        boltAnim = []
        for anim in ANIMATION_MONSTERHORYSONTAL:
            #boltAnim.append((anim, 0.3))
            boltAnim.append((ogre_images[0][0], 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()
         
    def update(self, platforms): # по принципу героя
                    
        self.image.fill(Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))
       
        self.rect.y += self.yvel
        self.rect.x += self.xvel
 
        self.collide(platforms)
        
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel =-self.xvel  # если прошли максимальное растояние, то идеи в обратную сторону
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p: # если с чем-то или кем-то столкнулись
               self.xvel = - self.xvel # то поворачиваем в обратную сторону
               self.yvel = - self.yvel
