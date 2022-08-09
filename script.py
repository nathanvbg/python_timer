import pygame
import time

def main():
	print("How long should the timer last ?")
	count = int(input())
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	
	clock = pygame.time.Clock()
	print(clock)
	time_init = 0
	running = True
	event = pygame.USEREVENT #custom event creation with ID 24
	pygame.time.set_timer(event, 1000)
	while running:
		for e in pygame.event.get():
			if e.type == event:
				print(count)
				count -= 1
				if count == -1:
					running = False
				#print(int(pygame.time.get_ticks() / 1000))
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					pygame.quit()
					running = False
			elif e.type == pygame.QUIT:
					pygame.quit()
					running = False

if __name__ == "__main__":
	main()