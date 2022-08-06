from pygame import gfxdraw
from setting import *
from random import randint

class Terrain():
	def __init__(self,start,end):
		self.body=Body(1,100,Body.KINEMATIC)
		self.body.position=0,Height/2
		self.shape=Segment(self.body,start,end,5)
		self.shape.elasticity=0
		self.shape.friction=200
		space.add(self.body,self.shape)
		
	def shift(self,camerax):
		self.body.position=camerax+self.body._get_position()[0],self.body._get_position()[1]
		
	def update(self,camerax):
		
		gfxdraw.line(screen,
		int(self.body.position[0]+self.shape.a[0]),
		int(self.body.position[1]+self.shape.a[1]),
		int(self.body.position[0]+self.shape.b[0]),
		int(self.body.position[1]+self.shape.b[1]),(255,255,0))
		
		self.shift(camerax)
		
		if self.body.position[0]+self.shape.b[0]<0:
			space.remove(self.body,self.shape)
			terrains.remove(self)
			
			terrains.append(Terrain((terrains[-1].shape.b[0]+terrains[-1].body.position[0],terrains[-1].shape.b[1]),(terrains[-1].shape.b[0]+seg_len,randint(-10,10))))