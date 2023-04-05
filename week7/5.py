import pygame 

from datetime import datetime 

res = w,h = 1200,800

pygame.init()
surface = pygame.display.set_mode(res)

clock =  pygame.display.Clock()

font = pygame.Sys.font.SysFont('Verdana',200)

check = True 

while check:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            check = False 
    surface.fill(pygame.Color('black')) 

    t = datetime.now()