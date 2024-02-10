import pygame  # Import the pygame module
import random

# Define constants for the screen dimensions
HEIGHT_OF_SCREEN = 1280
WIDTH_OF_SCREEN = 720
color = (255, 0, 0)
FPS = 30

pygame.init()  # Initialize pygame

# Initialize the canvas (screen) with the specified dimensions
canvas = pygame.display.set_mode((HEIGHT_OF_SCREEN, WIDTH_OF_SCREEN))

pygame.display.set_caption("blueSkies")  # Set the title of the canvas

clock = pygame.time.Clock()
exit = False  # Variable to control the main loop



# Main loop to handle events and update the display

while not exit:
	clock.tick(FPS)
	# Event handling loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  # If the user closes the window
			exit = True  # Set exit flag to True to exit the loop
	# retrieve_word('words.txt')
	# draw_clouds("yeah buddy")


	# Update the display
	pygame.display.update()

# Quit pygame when the loop exits
pygame.quit()
