import math,pygame,sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((720,480),0,32)
pygame.display.set_caption('雪花下落公开课')

# set up the colors
BLACK =(0,0,0)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

Background=pygame.image.load('bk.jpg').convert()
DISPLAYSURF.blit(Background,(0,0))

snowImg=pygame.image.load('snow.png')
snowx = 100
snowy = 100
direction = 'down'

fontObj = pygame.font.Font('freesansbold.ttf', 32) # 创建字体，freesansbold为字体格式，40为字体大小

textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)

textRectObj = textSurfaceObj.get_rect()

textRectObj.center = (100, 50)

for i in range(0,10)：
    snowx = random.randint(0,700)
    snowy = random.randint(0,460)
    DISPLAYSURF.blit(snowImg,(snowx,snowy))

# font= pygame.font.Font('simsum.ttc',40) # simsun 

# 创建文本
# text=font.render('*',True,(255,0,0)) # ''内为文本内容，True 表示开启抗锯齿，字体平滑，（255,0,0）为颜色。

while True: # main game loop
    
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
