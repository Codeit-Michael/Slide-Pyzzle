import pygame

pygame.init()

grid = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, None]
]


# Set up the Pygame window
pygame.init()
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

# Define the dimensions of the puzzle grid
grid_size = 3
tile_size = window_width // grid_size

# Loop through the puzzle grid and draw rectangles for each tile
for row in range(grid_size):
	for col in range(grid_size):
		tile_value = grid[row][col]  # Get the value of the current tile

		# Calculate the position of the tile on the window
		x = col * tile_size
		y = row * tile_size

		# Draw a rectangle for the tile
		pygame.draw.rect(window, (255, 255, 255), (x, y, tile_size, tile_size))  # Use white color for now

		# Add the tile value as text inside the rectangle
		font = pygame.font.Font(None, 30)
		text = font.render(str(tile_value), True, (0, 0, 0))  # Use black color for now
		text_rect = text.get_rect(center=(x + tile_size // 2, y + tile_size // 2))
		window.blit(text, text_rect)

		# Update the display
		pygame.display.flip()

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pygame.display.flip()
pygame.quit()