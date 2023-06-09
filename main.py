import pygame

from frame import Frame
from game import Game
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
		game = Game()
		while self.running:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

				if event.type == pygame.KEYDOWN:
					if game.arrow_key_clicked(event):
						frame.handle_click(event)

			self._draw(frame)
			self.FPS.tick(30)
	
		pygame.quit()


if __name__ == "__main__":
	window_size = (450, 550)
	screen = pygame.display.set_mode(window_size)
	pygame.display.set_caption("Slide Puzzle")

	game = Puzzle(screen)
	game.main(window_size[0])