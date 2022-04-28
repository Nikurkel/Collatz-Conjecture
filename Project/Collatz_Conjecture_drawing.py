import pygame
import random
import sys
import math
pygame.init()

WIDTH = 1600
HEIGHT = 900
frameRate = 0
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("times new roman", 20)

startAt = 0
debug = False

angle = 0.15
stepLength = 4


def handleTime():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.display.update()
	clock.tick(frameRate)

def conjecture(n):
	if n % 2 == 0:
		return int(n / 2)
	else:
		return (3 * n + 1) / 2

def offSet(rad):
	return (math.cos(rad), math.sin(rad))

def iteration(x):
	n = x
	count = 0
	maxN = n
	datapoints = []

	while n > 1:
		count += 1
		datapoints.append(n)
		n = conjecture(n)
		maxN = max(maxN, n)
		

	#pygame.draw.rect(window,(0,0,0),(0,0,WIDTH,HEIGHT))

	datapoints.reverse()
	rotation = 0
	position = (WIDTH/4, HEIGHT/2 + HEIGHT/10)
	c = (255 - random.randint(0,80), 150 - random.randint(0,60),150 - random.randint(0,40))
	for i in range(count):
		if datapoints[i] % 2 == 0:
			rotation += angle
		else:
			rotation -= angle
		p1 = position
		p2 = (position[0] + offSet(rotation)[0] * stepLength, position[1] + offSet(rotation)[1] * stepLength)
		position = p2

		pygame.draw.aaline(window, c, p1, p2, 255) #, 20 - int(i / count * 20))

	#txt = font.render(f"{datapoints}", True, (200,200,100))
	#window.blit(txt,(10,HEIGHT-30))

	if debug:
		print(datapoints)
		print(f"iterations: {count}")
		print(f"start n: {x}")
		print(f"max n: {maxN} \n")

def main():
	i = startAt
	while True:
		iteration(i)
		handleTime()
		i += 1

main()