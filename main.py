import pygame  # Import the pygame module
import random

# Define constants for the screen dimensions
HEIGHT_OF_SCREEN = 1280
WIDTH_OF_SCREEN = 720
FPS = 30
FILENAME = 'words.txt'

pygame.init()  # Initialize pygame

# Initialize the canvas (screen) with the specified dimensions
canvas = pygame.display.set_mode((HEIGHT_OF_SCREEN, WIDTH_OF_SCREEN))

pygame.display.set_caption("blueSkies")  # Set the title of the canvas

clock = pygame.time.Clock()
exit = False  # Variable to control the main loop


def retrieve_word(txt):
    with open(txt, 'r') as file:
        # Create an empty list to store the lines
        word_list = []

        # Iterate over the lines of the file
        for line in file:
            # Remove the newline character at the end of the line
            line = line.strip()

            # Append the line to the list
            word_list.append(line)

    for word in word_list:
        selected_word = word_list[random.randint(0, len(word_list) - 1)]
        return selected_word


def draw_clouds(word):
    color = (255, 0, 0)
    # Draw the red rectangle on the canvas
    pygame.draw.rect(canvas, color, pygame.Rect(30, 30, 60, 60), 2)
    print(word)


# Main loop to handle events and update the display

while not exit:
    clock.tick(FPS)
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user closes the window
            exit = True  # Set exit flag to True to exit the loop
    draw_clouds(retrieve_word(FILENAME))

    # Update the display
    pygame.display.update()

# Quit pygame when the loop exits
pygame.quit()
