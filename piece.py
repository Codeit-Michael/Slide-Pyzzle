"""PSEUDO CODE"""
import pygame

class Piece:
	def __init__(self, pin, piece_size):
		self.pin = pin
		self.piece_size = piece_size

		if self.pin != None:
			img_path = f'images/{pin}.png'
			self.img = pygame.image.load(img_path)
			self.img = pygame.transform.scale(self.img, (self.piece_size, self.piece_size))