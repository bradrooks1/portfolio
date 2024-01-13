import pygame

# Initialize Pygame
pygame.init()

# Create a display surface object
screen = pygame.display.set_mode((800, 600))

# Create a list of images to use in the animation
images = []
for i in range(10):
    images.append(pygame.image.load(f"frame_{i}.png"))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a variable to track the current frame
current_frame = 0

# Enter a game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the current frame
    current_frame = (current_frame + 1) % len(images)

    # Display the current frame
    screen.blit(images[current_frame], (0, 0))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
