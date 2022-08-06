from pygame import display,font,transform,image,time
from pymunk import *
from pymunk.constraints import *
from pymunk.pygame_util import DrawOptions
#screen setup
Width=800
Height=480
H_Width=Width//2
H_Height=Height//2
screen=display.set_mode((Width,Height))
#pymunk
space=Space()
space.gravity=0,1000
options=DrawOptions(screen)
#font & text
font=font.Font(None,30)
camerax=0
def cre_text(name,x,y):
	text=font.render(str(name),1,"red")
	screen.blit(text,(x,y))
#image
car_body=transform.scale(image.load("car-body.png"),(250,100)).convert_alpha()

car_wheel=transform.scale(image.load("car-wheel.png"),(60,60)).convert_alpha()
#time
clock=time.Clock()
terrains=[]
seg_len=50