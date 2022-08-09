import pygame
import time

height = 800
length = 800
text_height = 70
text_lenght = 70

def main():
	print("How long should the timer last ?")
	count = int(input())
	pygame.init()
	screen = pygame.display.set_mode((height, length))
	pygame.display.set_caption('Countdown timer')
	text_font = pygame.font.SysFont('arial', 50)
	
	running = True
	event = pygame.USEREVENT #custom event creation with ID 24
	pygame.time.set_timer(event, 1000)
	while running:
		screen.fill((255, 111, 0))
		for e in pygame.event.get():
			if e.type == event:
				if count != 0:
					count -= 1
				if count == 0:
					text_render = text_font.render("FINISHED!", True, (0, 0, 255))
				#print(int(pygame.time.get_ticks() / 1000))
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					#pygame.quit()
					running = False
			elif e.type == pygame.QUIT:
					#pygame.quit()
					running = False
		if count != 0:
			text_render = text_font.render(str(count), True, (0, 0, 255))
		screen.blit(text_render, ((height / 2 - text_height / 2), (length / 2 - text_lenght / 2)))
		pygame.display.flip()

if __name__ == "__main__":
	main()