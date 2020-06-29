#from classes import *
import pygame
from random import randrange

class indivdual:
	def __init__(self,x,y,r):
		#not implementing colouratm
		#self.colour = c
		self.posx = x
		self.posy = y
		self.radius = r

#initialize the pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
PopSize = 20
#taker = indivdual
def createPop(pop):
	Population = []
	for individuals in range(pop):
		pX = randrange(30,770)
		pY = randrange(30,570)
		radius = randrange(1,20)
		testind = indivdual(pX,pY,radius)
		Population.append(testind)
	return Population
def drawCircle(posX,posY,rad):
    #pygame.draw.circle(screen,(0,0,255), (50,50), 20) # Here <<<
    pygame.draw.circle(screen,(0,0,255),(posX,posY),rad)

InitialPop = createPop(PopSize)

# Game Loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255,150,0))
	for inds in range(0,len(InitialPop)):
		x = InitialPop[inds]
		#print InitialPop[inds].posx
		drawCircle(InitialPop[inds].posx,InitialPop[inds].posy,InitialPop[inds].radius)

	# 5  = 5 + -0.1 
	#drawCircle(10,15,12)
	pygame.display.update()
