#!/usr/bin/env python3
import pygame, sys
from pygame.locals import *

print("This is a simple etch-a-sketch program with pygame.")
print("us the arrow keys to control the position")

#initialize the starting Point
x=150
y=100

#init Pygame, set display resulution 
pygame.init()
screen = pygame.display.set_mode((300,200))


clock = pygame.time.Clock()
screen.fill((221,221,221)) #color light gray

print("Programm running...")

#Start main thread
while 1:
    clock.tick(60)
    pygame.draw.triangle(screen,(0,0,0), (x,y), 2)
    pygame.display.update()
   
   
    key=pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:x+=1
    if key[pygame.K_LEFT]:x-=1
    if key[pygame.K_UP]:y-=1
    if key[pygame.K_DOWN]:y+=1 
        
#Pygame helper functions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))

