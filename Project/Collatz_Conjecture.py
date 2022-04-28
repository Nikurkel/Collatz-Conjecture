import pygame
import random
import sys
import math
pygame.init()

WIDTH = 1600
HEIGHT = 900
frameRate = 3
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("times new roman", 20)

drawMode = 0 # 0 = raw, 1 = fit x, 2 = fit x/y
startAt = 10
debug = False

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
		return 3 * n + 1

def iteration(x):
	n = x
	count = 0
	maxN = n
	datapoints = [n]

	while n > 1:
		count += 1
		n = conjecture(n)
		maxN = max(maxN, n)
		datapoints.append(n)

	pygame.draw.rect(window,(0,0,0),(0,0,WIDTH,HEIGHT))

	for i in range(count):
		p1 = (0, 0)
		p2 = (0, 0)
		if drawMode == 0:
			p1 = ((i * 10), HEIGHT - datapoints[i])
			p2 = (((i + 1) * 10), HEIGHT - datapoints[i + 1])
		elif drawMode == 1:
			p1 = ((i / count * WIDTH), HEIGHT - datapoints[i])
			p2 = (((i + 1) / count * WIDTH), HEIGHT - datapoints[i + 1])
		elif drawMode == 2:
			p1 = ((i / count * WIDTH), HEIGHT - datapoints[i] / maxN * HEIGHT + 1 / maxN * HEIGHT)
			p2 = (((i + 1) / count * WIDTH), HEIGHT - datapoints[i + 1] / maxN * HEIGHT + 1 / maxN * HEIGHT)

		pygame.draw.aaline( window, (255,255,255), p1, p2)

	txt = font.render(f"{datapoints}", True, (200,200,100))
	window.blit(txt,(10,HEIGHT-30))

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