import pygame,sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('雪花下落公开课')
while True: # main game loop
    for event in pygame.event.get():
        if enent.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
