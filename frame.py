import pygame
import random

from cell import Cell
from piece import Piece

class Frame:
	def __init__(self, frame_size):
		self.grid_size = 3
		self.cell_width = frame_size // self.grid_size
		self.cell_height = frame_size // self.grid_size
		self.cell_size = (self.cell_width, self.cell_height)
		
		self.grid = self._generate_cell()
		self.pieces = self._generate_piece()

		self._setup()

	def _generate_cell(self):
		cells = []
		c_id = 0
		for col in range(self.grid_size):
			for row in range(self.grid_size):
				cells.append(Cell(row, col, self.cell_size, c_id))
				c_id += 1
		return cells

	def _generate_piece(self):
		puzzle_pieces = []
		p_id = 0
		for col in range(self.grid_size):
			for row in range(self.grid_size):
				puzzle_pieces.append(Piece(self.cell_size, p_id))
				p_id += 1
		return puzzle_pieces

	def _setup(self):
		for cell in self.grid:
			piece_choice = random.choice(self.pieces)
			cell.occupying_piece = piece_choice
			self.pieces.remove(piece_choice)

	# 2nd wave pseudo
	def handle_click(self):
		pass

	# 2nd wave pseudo
	def get_moves(self):
		pass

	def draw(self, display):
		for cell in self.grid:
			cell.draw(display)
