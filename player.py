from setting import *
from math import degrees

class Player:
	def __init__(self):
		self.body_img=car_body
		self.wheel_img=car_wheel
		#body
		self.body=Body(5,450*5)
		self.body.position=300,Height/3
		self.shape=Poly.create_box(self.body,(car_body.get_width()/2,car_body.get_height()/2))
		self.shape.elasticity=0.1
		self.shape.friction=1
		self.shape.filter=ShapeFilter(1)
		space.add(self.body,self.shape)
		#front wheel
		self.f_wheel_body=Body(1,200)
		self.f_wheel_body.position=100,Height/3
		self.f_wheel_shape=Circle(self.f_wheel_body,car_wheel.get_width()/2)
		self.f_wheel_shape.elasticity=0.1
		self.f_wheel_shape.friction=200
		self.f_wheel_shape.filter=ShapeFilter(1)
		self.f_pin=PivotJoint(self.body,self.f_wheel_body,(80,30),(0,0))
		space.add(self.f_wheel_body,self.f_wheel_shape,self.f_pin)
		#back wheel
		self.b_wheel_body=Body(1,200)
		self.b_wheel_body.position=100,Height/3
		self.b_wheel_shape=Circle(self.b_wheel_body,30)
		self.b_wheel_shape.elasticity=0.1
		self.b_wheel_shape.friction=200
		self.b_wheel_shape.filter=ShapeFilter(1)
		self.b_pin=PivotJoint(self.body,self.b_wheel_body,(-80,30),(0,0))
		space.add(self.b_wheel_body,self.b_wheel_shape,self.b_pin)
		
		self.is_move=0
		self.speed=0
		
	def get_input(self,down,up,fingerx):
		if down:
			self.is_move=1
			if fingerx>H_Width:
				self.speed=10
			if fingerx<H_Width:
				self.speed=-10
		if up:
			self.is_move=0
			self.speed=0
			
	def movenment(self):
		if -1000<self.b_wheel_body.angular_velocity<1000:
			self.b_wheel_body.angular_velocity+=self.speed
		
	def draw(self):
		render_car_body=transform.rotate(car_body,-degrees(self.body.angle))
		
		screen.blit(render_car_body,(self.body.position[0]-render_car_body.get_width()/2,self.body.position[1]-render_car_body.get_height()/2-20))
		
		render_f_wheel=transform.rotate(car_wheel,-degrees(self.f_wheel_body.angle))
		
		screen.blit(render_f_wheel,(self.f_wheel_body.position[0]-render_f_wheel.get_width()/2,self.f_wheel_body.position[1]-render_f_wheel.get_height()/2))
		
		render_b_wheel=transform.rotate(car_wheel,-degrees(self.b_wheel_body.angle))
		
		screen.blit(render_b_wheel,(self.b_wheel_body.position[0]-render_b_wheel.get_width()/2,self.b_wheel_body.position[1]-render_b_wheel.get_height()/2))
		
	def shift(self,camerax):
		self.body.position=camerax+self.body._get_position()[0],self.body._get_position()[1]
		
		self.f_wheel_body.position=camerax+self.f_wheel_body._get_position()[0],self.f_wheel_body._get_position()[1]
		
		self.b_wheel_body.position=camerax+self.b_wheel_body._get_position()[0],self.b_wheel_body._get_position()[1]
		
	def update(self,camerax):
		self.draw()
		self.shift(camerax)
		self.movenment()
		