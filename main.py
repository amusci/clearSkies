import pygame
import random

# Define constants for the screen dimensions
HEIGHT_OF_SCREEN = 1280
WIDTH_OF_SCREEN = 720
FPS = 30
FILENAME = 'words.txt'
CLOUD_SPEED = 5

pygame.init()  # Initialize pygame

# Initialize the canvas (screen) with the specified dimensions
canvas = pygame.display.set_mode((HEIGHT_OF_SCREEN, WIDTH_OF_SCREEN))

pygame.display.set_caption("blueSkies")  # Set the title of the canvas

clock = pygame.time.Clock()
exit = False  # Variable to control the main loop


# Function to retrieve a random word from a text file
def retrieve_word(txt):
    with open(txt, 'r') as file:
        word_list = [line.strip() for line in file]
    return random.choice(word_list)


# Function to draw clouds and print a word every 10 seconds
def draw_clouds(word):
    # Generate random RGB values for the color
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    # Draw the colored rectangle on the canvas
    pygame.draw.rect(canvas, color, pygame.Rect(30, 30, 200, 100), 2)

    # Create a font object
    font = pygame.font.Font(None, 36)  # Default font, size 36

    # Render the word as text
    text = font.render(word, True, (255, 255, 255))  # Render with white color

    # Calculate the position to center the text in the rectangle
    text_rect = text.get_rect(center=(130, 80))  # Centered horizontally and vertically

    # Blit the rendered text onto the canvas
    canvas.blit(text, text_rect)


# Main loop to handle events and update the display
start_time = pygame.time.get_ticks()  # Get the initial time
while not exit:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Get the current time in milliseconds
    current_time = pygame.time.get_ticks()

    # Calculate the elapsed time in seconds
    elapsed_time = (current_time - start_time) / 1000

    # Print a new word every 5 seconds
    if elapsed_time >= 1:
        draw_clouds(retrieve_word(FILENAME))
        start_time = current_time  # Reset the start time

    # Update the display
    pygame.display.update()

# Quit pygame when the loop exits
pygame.quit()
