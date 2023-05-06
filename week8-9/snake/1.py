import pygame
pygame.init()
 
monitor = pygame.display.set_mode((800,800))
pygame.display.set_caption("bastadynba Era ")
icon  = pygame.image.load('/Users/zeinaddinzurgambayev/pp2/week8/racer/image/car2.png') 
pygame.display.set_icon(icon)

squar = pygame.Surface((500,350)) 
icon = pygame.image.load() 
check = True

while check:
    pygame.display.update()
    monitor.blit(squar)
    pygame.draw.circle(screen) 


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = False
            pygame.quit()