# Example file showing a basic pygame "game loop"
import pygame
import os

# pygame setup
pygame.init()

# Constants
black = pygame.Color(5, 5, 5)
orange = pygame.Color(245, 120, 2)
screen_width = 1000
screen_height = 1000
asset_width = 256
asset_height = 256
space_between = 64
margin = (screen_width - (asset_width * 3 + space_between * 2)) / 2

# Setup
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Assets
lovly_sissors = pygame.image.load(os.path.join("assets", "sissors.png"))
lovly_paper = pygame.image.load(os.path.join("assets", "paper.png"))
lovly_stone = pygame.image.load(os.path.join("assets", "stone.png"))

icons = [lovly_stone, lovly_paper, lovly_sissors]

# In-game state
running = True
selected_item = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RIGHT:
                selected_item += 1
            elif event.key == pygame.K_LEFT:
                selected_item -= 1

            if selected_item > 2:
                selected_item = 0
            elif selected_item < 0:
                selected_item = 2
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    for iter in enumerate(icons):
        x = margin + (asset_width + space_between) * iter[0]
        y = (screen_height - asset_height)/2
        pygame.draw.rect(screen, orange, pygame.Rect((x, y), (asset_width, asset_height)))
        screen.blit(iter[1], dest=(x, y))

        if iter[0] == selected_item:
            points = [
                (x, y),
                (x + asset_width, y),
                (x + asset_width, y + asset_height),
                (x, y + asset_height),
            ]
            pygame.draw.lines(screen, black, closed=True, points=points, width=10)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()
