"""PSEUDO CODE"""
import pygame
from . import Tile
from . import Piece

class Frame:
	def __init__(self, tile_size):
		self.tile_size = tile_size
		
		self.grid = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, None]
		]
		self.piece = {}

		self.setup()

	def setup(self):
		pass

	# 2nd wave pseudo
	def handle_click(self):
		pass

	# 2nd wave pseudo
	def get_moves(self):
		pass

	def draw(self):
		for tile in self.tile_list:
			tile.draw(display)