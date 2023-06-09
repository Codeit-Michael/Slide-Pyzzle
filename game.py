import pygame

class Game:

	def arrow_key_clicked(self, click):
		try:
			if click.key == pygame.K_LEFT or click.key == pygame.K_RIGHT or click.key == pygame.K_UP or click.key == pygame.K_DOWN:
				return(True)
		except:
			return(False)

	def is_game_over(self, frame):
		for cell in frame.grid:
			piece_id = cell.occupying_piece.p_id
			# print(piece_id, cell.c_id)
			if cell.c_id == piece_id:
				is_arranged = True
			else:
				is_arranged = False
				break
		return is_arranged

	def message(self):
		print("YOU WIN!!")