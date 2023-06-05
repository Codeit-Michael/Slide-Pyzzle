import pygame

from frame import Frame

pygame.init()

class Puzzle:
	def __init__(self, screen):
		self.screen = screen
		self.running = True
		self.FPS = pygame.time.Clock()

	def _draw(self, frame):
		frame.draw(self.screen)
		pygame.display.update()

	def main(self, frame_size):
		self.screen.fill("white")
		frame = Frame(frame_size)
		while self.running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
			
			self._draw(frame)
			self.FPS.tick(30)
	
		pygame.quit()


if __name__ == "__main__":
	window_size = (450, 550)
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption("Slide Puzzle")

	game = Puzzle(screen)
	game.main(window_size[0])