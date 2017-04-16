'''Author:Dustni'''
import pygame
from pygame.locals import *
from sys import exit
import time
import receive
import gv
import fan_c
import dill as pickle

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if( x+w > mouse[0] > x) and( y+h > mouse[1] > y):
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            
            action() 
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf= smallText.render(str(msg), True, BLACK)
    textRect=textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)




def draw_single(order,temper):
    draw_x=10+70*order
    draw_y=280+200-scale_temp*temper
    draw_width=70
    draw_height=scale_temp*temper
    rect_list=[draw_x,draw_y,draw_width,draw_height]
    pygame.draw.rect(screen,[255,10*(10-order),0],rect_list,0)

def update_draw(draw_list,new_value):
    old_list=draw_list
    for i in range(len(draw_list)):
        if(i!=len(draw_list)-1):
            draw_list[i][1]=old_list[i+1][1]
        else:
            draw_list[i][1]=new_value
def draw():
    for i in range(len(draw_list)):
        draw_single(draw_list[i][0],draw_list[i][1])

def draw_gui():
    pygame.draw.line(screen, YELLOW, (0,280+200-scale_temp*gv.warn_line), (720,280+200-scale_temp*gv.warn_line),1)

    warn_temp_font = fontObj.render(str(gv.warn_line), True, YELLOW, BLUE)
    warn_temp_obj = warn_temp_font.get_rect()
    warn_temp_obj.center = (20, 280+200-scale_temp*gv.warn_line)
    screen.blit(warn_temp_font, warn_temp_obj)

    fan_speed_font = fontObj_2.render('Fan speed: '+str(fan_speed), True, WHITE, BLUE)
    fan_speed_font_obj = fan_speed_font.get_rect()
    fan_speed_font_obj.center = (360, 160)
    screen.blit(fan_speed_font, fan_speed_font_obj)

    button('-',300,180,50,50,GREEN,YELLOW,action=decrease_warn_line)
    button('+',370,180,50,50,RED,YELLOW,action=add_warn_line)


def add_warn_line():
    
    gv.warn_line+=1
    file_object = open('data.txt', 'w')
    file_object.write(str(gv.warn_line))
    file_object.close( )
 
    return gv.warn_line

def decrease_warn_line():
    gv.warn_line-=1
    file_object = open('data.txt', 'w')
    file_object.write(str(gv.warn_line))
    file_object.close()
    return gv.warn_line

def warn(x):
    global warn_state
    global fan_speed
    if(x>=gv.warn_line):
        warn_font = fontObj.render('Warning!!!Over heating!!!', True, RED, BLUE)
        warn_font_obj = warn_font.get_rect()
        warn_font_obj.center = (360, 250)
        screen.blit(warn_font, warn_font_obj)

        if(warn_state==False):
            warn_state=True
            fan_c.fan_open()
            fan_speed=update_fan_spd(x)
        else:
            fan_speed = update_fan_spd(x)
    else:
        warn_state=False
        fan_c.fan_close()
        fan_speed=0

    return True




def update_fan_spd(temper):
    return _model.evaluate([gv.warn_line,temper])

max_temp=50
scale_temp=200/max_temp       


warn_state= False
fan_speed=0
draw_list=[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]]

BLUE = (0, 0 ,128) 
GREEN = (0, 255, 0) 
YELLOW=(255,255,0)
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
pygame.init()

screen = pygame.display.set_mode((720, 480), FULLSCREEN, 32)
#screen = pygame.display.set_mode((720, 480), False, 32)
fontObj = pygame.font.Font('freesansbold.ttf', 32)
fontObj_2 = pygame.font.Font('freesansbold.ttf', 16)
# pygame.mouse.set_visible(False)
with open("gptree.pkl", 'rb') as f:
    _model = pickle.load(f)

while True:
    temper=receive.get_temper()
    
    nowtime=time.asctime( time.localtime(time.time()) )
    textSurfaceObj = fontObj_2.render(nowtime, True, YELLOW, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (360, 140)

    textSurfaceObj_2 = fontObj.render('Temperature: '+temper+' degrees ', True, GREEN, BLUE)
    textRectObj_2 = textSurfaceObj_2.get_rect()
    textRectObj_2.center = (360, 100)


    screen.fill(BLUE)
    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj_2, textRectObj_2)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key==K_q:
                pygame.quit()
                exit()
  

    update_draw(draw_list,float(temper))
    
    warn(float(temper))
    draw()
    draw_gui()
    pygame.display.update()

