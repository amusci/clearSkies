import pygame
import random

# GLOBAL
HEIGHT_OF_SCREEN = 1280
WIDTH_OF_SCREEN = 720
FPS = 30
FILENAME = 'words.txt'
CLOUD_SPEED = 5

# NORMAL

user_text = ''
input_rect = pygame.Rect(200, 200, 140, 32)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')

active = False

pygame.init()  # Initialize pygame
base_font = pygame.font.Font(None, 32)

# Initialize the canvas (screen) with the specified dimensions
canvas = pygame.display.set_mode((HEIGHT_OF_SCREEN, WIDTH_OF_SCREEN))

pygame.display.set_caption("clearSkies")  # Set the title of the canvas

clock = pygame.time.Clock()
exit = False  # Variable to control the main loop


# Function to retrieve a random word from a text file
def retrieve_word(txt):
    with open(txt, 'r') as file:
        word_list = [line.strip() for line in file]
    return random.choice(word_list)


# Function to draw clouds and print a word every 5 seconds
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

    # Draw a filled black rectangle over the entire area where the text will be rendered
    pygame.draw.rect(canvas, (0, 0, 0), pygame.Rect(32, 32, 196, 96))

    # Blit the rendered text onto the canvas
    canvas.blit(text, text_rect)


def user_input():
    pass


# Main loop to handle events and update the display
start_time = pygame.time.get_ticks()  # Get the initial time
while not exit:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:

                user_text = user_text[:-1]

            else:
                user_text += event.unicode

    if active:
        color = color_active
    else:
        color = color_passive

        # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(canvas, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    # render at position stated in arguments
    canvas.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()

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
