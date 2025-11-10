# Example file showing a basic pygame "game loop"
import pygame
import os
import random

# pygame setup
pygame.init()

# Constants
black = pygame.Color(5, 5, 5)
orange = pygame.Color(245, 120, 2, a=255)
AL_orange = pygame.Color(245, 120, 2, a=255)
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
timerRock = 0
timerPaper = 0
timerSissors = 0
start_timerRock = False
start_timerPaper = False
start_timerSissors = False
locked = False

while running:
    deltaTime = clock.get_time() / 1000

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
            if locked == False:
                if event.key == pygame.K_RIGHT:
                    selected_item += 1
                elif event.key == pygame.K_LEFT:
                    selected_item -= 1

            if selected_item > 2:
                selected_item = 0
            elif selected_item < 0:
                selected_item = 2

            if event.key == pygame.K_SPACE and selected_item == 0 and timerRock == 0 or timerRock >= 1.5:
                start_timerRock = True
                timer = 0
                locked = True

            if event.key == pygame.K_SPACE and selected_item == 1 and timerPaper == 0 or timerPaper >= 1.5:
                start_timerPaper = True
                timer = 0
                locked = True

            if event.key == pygame.K_SPACE and selected_item == 2 and timerSissors == 0 or timerSissors >= 1.5:
                start_timerSissors = True
                timer = 0
                locked = True

    # fading the icons
    fade_alpha = 255

    if start_timerRock:
        timerRock += 1 / 60
        lovly_sissors.set_alpha(max(0, 255 - (timerRock / 1.5 * 255)))
        lovly_paper.set_alpha(max(0, 255 - (timerRock / 1.5 * 255)))
        fade_alpha = max(0, 255 - (timerSissors / 1.5 * 255))
        if timerRock >= 1.5:
            start_timerRock = False
            lovly_paper.set_alpha(0)
            lovly_sissors.set_alpha(0)

    if start_timerPaper:
        timerPaper += 1 / 60
        lovly_sissors.set_alpha(max(0, 255 - (timerPaper / 1.5 * 255)))
        lovly_stone.set_alpha(max(0, 255 - (timerPaper / 1.5 * 255)))
        fade_alpha = max(0, 255 - (timerSissors / 1.5 * 255))
        if timerPaper >= 1.5:
            start_timerPaper = False
            lovly_stone.set_alpha(0)
            lovly_sissors.set_alpha(0)

    if start_timerSissors:
        timerSissors += 1 / 60
        lovly_stone.set_alpha(max(0, 255 - (timerSissors / 1.5 * 255)))
        lovly_paper.set_alpha(max(0, 255 - (timerSissors / 1.5 * 255)))
        fade_alpha = max(0, 255 - (timerSissors / 1.5 * 255))
        if timerSissors >= 1.5:
            start_timerRock = False
            lovly_paper.set_alpha(0)
            lovly_stone.set_alpha(0)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    
    # RENDER YOUR GAME HERE
    for iter in enumerate(icons):
        x = margin + (asset_width + space_between) * iter[0]
        y = (screen_height - asset_height) - 150
        pygame.draw.rect(screen, orange, pygame.Rect((x, y), (asset_width, asset_height)))
        screen.blit(iter[1], dest=(x, y))
        
        pygame.draw.rect(screen, AL_orange, pygame.Rect((margin + asset_width + space_between, 100), (asset_width, asset_height)))
        screen.blit(lovly_paper, dest=(margin + asset_width + space_between, 100))

        orange_surface = pygame.Surface((asset_width, asset_height), pygame.SRCALPHA)
        orange_surface.fill((*orange, fade_alpha))

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