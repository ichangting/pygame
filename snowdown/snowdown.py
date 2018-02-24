# 准备材料和工具
import pygame,sys,random  
from pygame.locals import *

# 初始化
pygame.init() 

# 设置窗口和标题
screen = pygame.display.set_mode((700,460),0,32)
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
snow = [] # 空的雪花列表
x=[]
y=[]

for i in range(0,100):
    # 创建字体格式
    font = pygame.font.Font("simsun.ttc",random.randint(10,50))
    # 把做好的雪花放到列表中
    snow.append(font.render("*",True,WHITE))
    # ''内为文本内容，True 表示开启抗锯齿，字体平滑。
    x.append(random.randint(0,700))
    y.append(random.randint(0,460))

while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(Background,(0,0)) # 给窗口填上背景

    # 将雪花贴到窗口中
    for i in range(0,100):
        screen.blit(snow[i],(x[i],y[i]))

    # 控制雪花下落
    for i in range(0,100):
        y[i] = y[i]+0.1
        if y[i]>600:
            y[i]=0
            x[i]= random.randint(0,800)

    # 刷新屏幕
    pygame.display.update()
