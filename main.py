"""PSEUDO CODE"""
import pygame

pygame.init()

class Puzzle:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.FPS = pygame.time.Clock()

	def main(self):
		self.screen.fill("white")
		while self.running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			
			pygame.display.flip()
			self.FPS.tick(30)
	
		pygame.quit()


if __name__ == "__main__":
	window_size = (450, 550)
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption("Slide Puzzle")

	game = Puzzle(screen)
	game.main()