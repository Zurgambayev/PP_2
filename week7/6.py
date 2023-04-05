import pygame
import datetime 

pygame.init()
angle = 0
def rotate(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
    return rotated_image, rotated_rect

monitor = pygame.display.set_mode((829,836))


mici = pygame.image.load('/Users/zeinaddinzurgambayev/pp2/week7/Новая папка/main-clock.png')
mici_left  = pygame.image.load('/Users/zeinaddinzurgambayev/pp2/week7/Новая папка/left-hand.png')



mici_right  = pygame.image.load('/Users/zeinaddinzurgambayev/pp2/week7/Новая папка/right-hand.png')
clock = pygame.time.Clock()



check = True 


while check:       
    angle = angle + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
    pygame.display.update()