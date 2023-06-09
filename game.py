import pygame

class Game:

	def arrow_key_clicked(self, click):
		try:
			num_list = (79, 80, 81, 82)
			if click.key == pygame.K_LEFT or click.key == pygame.K_RIGHT or click.key == pygame.K_UP or click.key == pygame.K_DOWN:
				return(True)
		except:
			return(False)

	
	# def is_game_over(self, frame):
	# 	is_arranged = False
	# 	for tile in frame.tile_list:
	# 		piece_pin = tile.occupying_piece.pin
	# 		if tile.pin == piece_pin:
	# 			arranged = True
	# 		else:
	# 			arranged = False:
	# 			break
	# 	return is_arranged