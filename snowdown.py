import pygame,sys,random
from pygame.locals import *

pygame.init()

# 设置窗口和标题
DISPLAYSURF = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('雪花下落公开课')

# 设置颜色，RGB模式
BLACK =(0,0,0)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# 添加背景
Background=pygame.image.load('bk.jpg').convert()

# 添加雪花
snowImg=pygame.image.load('snow.png').convert_alpha()
snowrect = snowImg.get_rect()
width,height = snowImg.get_size()

for i in range(0,10):
    snowx = random.randint(0,800)
    snowy = random.randint(0,200)
    DISPLAYSURF.blit(snowImg,(snowx,snowy)) 

    
# 设置速度
speed =[0,20]

# 设置屏幕的帧率
fps = 30
fclock = pygame.time.Clock()

# font= pygame.font.Font('simsum.ttc',40) # simsun 

# 创建文本
# text=font.render('*',True,(255,0,0)) # ''内为文本内容，True 表示开启抗锯齿，字体平滑，（255,0,0）为颜色。

while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(Background,(0,0))

    DISPLAYSURF.blit(snowImg,(snowx,snowy))
    snowy +=50
    if snowy > 600:
        snowy = 0
    pygame.display.update()
    fclock.tick(fps)
