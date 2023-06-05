"""PSEUDO CODE"""
import pygame

class Game:
	
	def is_game_over(self, frame):
		is_arranged = False
		for tile in frame.tile_list:
			piece_pin = tile.occupying_piece.pin
			if tile.pin == piece_pin:
				arranged = True
			else:
				arranged = False:
				break
		return is_arranged