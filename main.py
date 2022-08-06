from pygame import init,event,FINGERDOWN,FINGERUP
init()
from setting import *
from player import Player
from terrain import Terrain
from random import randint

class Game:
	def __init__(self):
		#player setup
		self.player=Player()
		#terrain setup
		terrains.append(Terrain((0,0),(0,randint(-10,10))))
		for i in range(Width//seg_len):
			terrains.append(Terrain((terrains[-1].shape.b[0]+terrains[-1].body.position[0],terrains[-1].shape.b[1]),(i*50,randint(-10,10))))
		#touch setup
		self.fingerx=0
		self.fingery=0
		
		self.left_fingerx=0
		self.left_fingery=0
		
		self.right_fingerx=0
		self.right_fingery=0
		#camera setup
		self.camerax=0
		
	def update(self):
		self.player.update(self.camerax)
		
		for terrain in terrains:
			terrain.update(self.camerax)
			
		self.camerax=(Width/3)+-self.player.body.position[0]
		
	def loop(self):
		while 1:
			clock.tick(0)
			screen.fill((50,50,50))
			for ev in event.get():
				if ev.type==FINGERDOWN or ev.type==FINGERUP:
					self.fingerx=ev.x*Width
					self.fingery=ev.y*Height
					
				self.player.get_input(ev.type==FINGERDOWN or ev.type==FINGERDOWN,ev.type==FINGERUP,self.fingerx)
			
			self.update()
			
			cre_text(clock.get_fps(),0,0)
			cre_text(str(terrains[0].shape.b[0]//100)+"m",0,100)
			space.debug_draw(options)
			display.update()
			space.step(1/60)

if __name__=="__main__":
	game=Game()
	game.loop()