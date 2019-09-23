import pygame
from constants import pygameWindowWidth, pygameWindowDepth
class PYGAME_WINDOW:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((pygameWindowWidth,pygameWindowDepth))
	def Prepare(self):
		pygame.event.get()
		white = (255,255,255)
		self.screen.fill(white)
	def Reveal(self):
		pygame.display.update()
	def Draw_Black_Circle(self,x,y):
		pygame.draw.circle(self.screen,(0,0,0),(x,y),20)
	def Draw_Black_Line(self,base_x,base_y,tip_x,tip_y):
		pygame.draw.line(self.screen,(0,0,0),(base_x,base_y),(tip_x,tip_y),5)
