import pygame

class Piece:
	def __init__(self, p_id, piece_size):
		self.p_id = p_id
		self.piece_size = piece_size

		if self.p_id != 8:
			img_path = f'puzz-pieces/{self.p_id}.jpg'
			self.img = pygame.image.load(img_path)
			self.img = pygame.transform.scale(self.img, (self.piece_size, self.piece_size))