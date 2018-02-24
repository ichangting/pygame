# 这是一个Pygame的基础教程
import math,pygame,sys  # 导入需要的库
from pygame.locals import *  # 引入pygame中的所有常量

pygame.init()  # 初始化

# set up the window
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Pygame基础教程')

# 设置颜色 RGB
BLACK =(0,0,0)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

# 创建字体
myfont= pygame.font.Font('simsun.ttc',40) # simsun 为字体格式，40为字体大小

# 创建文本图像
textImg = myfont.render("Hello Pygame", True, WHITE)
# ''内为文本内容，True 表示开启抗锯齿，字体平滑，（255,0,0）为颜色。

# 绘制一个圆形,需要的参数有：
color = WHITE
position = 400,300 # 圆心的位置
radius = 100  # 圆的半径
width = 10  # 圆圈的宽度

# 绘制一个矩形
pos_x = 350
pos_y = 250

vel_x = 2
vel_y = 1

# 绘制线条
width_line = 8 # 线条宽度

while True: # main game loop
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    # 按Esc则退出游戏
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    screen.fill(BLACK)          
    screen.blit(textImg,(100,100))  # 绘制文本图像

    # 绘制圆形
    pygame.draw.circle(screen, color, position, radius, width) # 绘制一个圆形

    # 绘制线条
    pygame.draw.line(screen, BLUE,(300,300),(500,300), width_line)

    #绘制弧形的代码
    position_arc = 200,150,200,200  # 矩形，表示弧形的边界
    start_angle = math.radians(0)  # 起始角度
    end_angle = math.radians(180)  # 结束角度
    width = 8
    pygame.draw.arc(screen, GREEN, position_arc, start_angle, end_angle, width)
    
    # 移动矩形
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 700 or pos_x<0:
        vel_x = - vel_x
    if pos_y > 500 or pos_y<0:
        vel_y = - vel_y

    pos = pos_x, pos_y, 100,100
    pygame.draw.rect(screen, BLUE, pos,0)
    
    pygame.display.update()
    
