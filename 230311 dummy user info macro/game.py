import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the game window
game_window = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("My Game")

# Create a clock object to control the game's frame rate
clock = pygame.time.Clock()

# Set up the game loop
game_running = True
while game_running:

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Clear the screen
    game_window.fill((255, 255, 255))

    # Draw a rectangle
    rect = pygame.Rect(50, 50, 100, 100)
    pygame.draw.rect(game_window, (255, 0, 0), rect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
