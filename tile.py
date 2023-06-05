"""PSEUDO CODE"""
import pygame

class Tile:
	def __init__(self, col, row, pin, tile_size):
		self.col = col
		self.row = row
		self.pin = pin
		self.tile_size = tile_size
		self.occupying_piece = None

	def draw(self):
		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)