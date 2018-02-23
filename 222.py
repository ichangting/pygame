#这个窗口是写代码的地方--注释
#准备材料和工具
import pygame #导入一个pygame=python+game做python游戏编程的工具库
import random #导入随机数工具库
#消息通知，告诉程序工具库准备完毕
pygame.init()

#做准备工作的地方
#创建窗口
sc=pygame.display.set_mode((700,460)) #尺寸:宽高成对

# 导入背景
pygame.image.load('bk.jpg')

#创建雪花列表
snow=[] #空的雪花列表
x=[]
y=[]

for i in range(0,100):
    #创建字体格式
    font=pygame.font.Font("simsun.ttc",random.randint(10,50))
    #把做好的雪花放到列表中
    snow.append(font.render("*",True,(255,255,255)))
    x.append(random.randint(0,700))
    y.append(random.randint(0,460))
while True:
    #窗口填充为黑色
    sc.fill((0,0,255)) #(0,0)坐标
    #将雪花贴到窗口中
    for i in range(0,100):
        sc.blit(snow[i],(x[i],y[i]))
    #控制坐标实现雪花下落
    for i in range(0,100):
        y[i]=y[i]+0.1
        if y[i]>460:
            y[i]=0
            x[i]=random.randint(0,700)
    #窗口屏幕刷新
    pygame.display.update()
