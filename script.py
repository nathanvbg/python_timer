import pygame
import time

def main():
	print("How long should the timer last ?")
	total_sec = int(input())
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	
	#clock = pygame.time.Clock()
	#print(clock)
	time_init = 0
	running = True
	t = 3
	while (running and total_sec > 0):
		time.sleep(1)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					running = False
			elif event.type == pygame.QUIT:
					pygame.quit()
					running = False
			print(pygame.time.get_ticks())
			if(pygame.time.get_ticks() > time * 1000):
				print('finiiii')

if __name__ == "__main__":
	main()