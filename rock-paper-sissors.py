# Example file showing a basic pygame "game loop"
import pygame
import os
import random
from turning_things_into_functions import fadingEfect, activator, handle_fade


class GameState:
    def __init__(self):
        self.selected_item = 1
        self.running = True
        self.timer = 0
        self.fade_alpha = 255
        self.fading_active = False


# pygame setup
pygame.init()

# Constants
black = pygame.Color(5, 5, 5)
orange = pygame.Color(245, 120, 2, a=255)
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

sissors = pygame.image.load(os.path.join("assets", "sissors.png"))
paper = pygame.image.load(os.path.join("assets", "paper.png"))
stone = pygame.image.load(os.path.join("assets", "stone.png"))

icons = [lovly_stone, lovly_paper, lovly_sissors]

# In-game state
state = GameState()

running = True
selected_item = 1
timerRock = 0
timerPaper = 0
timerSissors = 0
start_timerRock = False
start_timerPaper = False
start_timerSissors = False
locked = False
fade_alpha = 255
accu = "rock"
timerAL = 0

while running:
    deltaTime = clock.get_time() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if not locked:
                if event.key == pygame.K_RIGHT:
                    selected_item += 1
                elif event.key == pygame.K_LEFT:
                    selected_item -= 1

            if selected_item > 2:
                selected_item = 0
            elif selected_item < 0:
                selected_item = 2

            if event.key == pygame.K_SPACE:
                activator(1, state, lovly_sissors, lovly_stone, event)

            # if locked == False:
            #     if event.key == pygame.K_SPACE and selected_item == 0 and (timerRock == 0 or timerRock >= 1.5):
            #         start_timerRock = True
            #         timerRock = 0
            #         locked = True

            #     if event.key == pygame.K_SPACE and selected_item == 1 and (timerPaper == 0 or timerPaper >= 1.5):
            #         start_timerPaper = True
            #         timerPaper = 0
            #         locked = True

            #     if event.key == pygame.K_SPACE and selected_item == 2 and (timerSissors == 0 or timerSissors >= 1.5):
            #         start_timerSissors = True
            #         timerSissors = 0
            #         locked = True

    # fading the icons and orange
    handle_fade(lovly_sissors, lovly_stone, state)

    # if start_timerRock:
    #     timerRock += 1 / 60
    #     lovly_sissors.set_alpha(max(0, 255 - (timerRock / 1.5 * 255)))
    #     lovly_paper.set_alpha(max(0, 255 - (timerRock / 1.5 * 255)))
    #     fade_alpha = int(max(0, 255 - (timerRock / 1.5 * 255)))
    #     if timerRock >= 1.5:
    #         start_timerRock = False
    #         lovly_paper.set_alpha(0)
    #         lovly_sissors.set_alpha(0)
    #         fade_alpha = 0

    # if start_timerPaper:
    #     timerPaper += 1 / 60
    #     lovly_sissors.set_alpha(max(0, 255 - (timerPaper / 1.5 * 255)))
    #     lovly_stone.set_alpha(max(0, 255 - (timerPaper / 1.5 * 255)))
    #     fade_alpha = int(max(0, 255 - (timerPaper / 1.5 * 255)))
    #     if timerPaper >= 1.5:
    #         start_timerPaper = False
    #         lovly_sissors.set_alpha(0)
    #         lovly_stone.set_alpha(0)

    # if start_timerSissors:
    #     timerSissors += 1 / 60
    #     lovly_stone.set_alpha(max(0, 255 - (timerSissors / 1.5 * 255)))
    #     lovly_paper.set_alpha(max(0, 255 - (timerSissors / 1.5 * 255)))
    #     fade_alpha = int(max(0, 255 - (timerSissors / 1.5 * 255)))
    #     if timerSissors >= 1.5:
    #         start_timerSissors = False
    #         lovly_paper.set_alpha(0)
    #         lovly_stone.set_alpha(0)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    timerAL += 1 / 60
    if timerAL >= 1 / 3:
        if accu == "rock":
            accu = "paper"
            timerAL = 0
        elif accu == "paper":
            accu = "sissors"
            timerAL = 0
        else:
            accu = "rock"
            timerAL = 0

    # RENDER YOUR GAME HERE
    for iter in enumerate(icons):
        x = margin + (asset_width + space_between) * iter[0]
        y = (screen_height - asset_height) - 150

        # create fading orange surface with alpha
        # wtf
        orange_surface = pygame.Surface(
            (asset_width, asset_height), pygame.SRCALPHA)
        orange_surface.fill((orange.r, orange.g, orange.b, fade_alpha))
        screen.blit(orange_surface, (x, y))

        # blit icons as before
        screen.blit(iter[1], dest=(x, y))

        # second static orange rect (unchanged)
        pygame.draw.rect(screen, orange, pygame.Rect(
            (margin + asset_width + space_between, 100), (asset_width, asset_height)))
        if accu == "rock":
            screen.blit(stone, dest=(
                margin + asset_width + space_between, 100))
        elif accu == "paper":
            screen.blit(paper, dest=(
                margin + asset_width + space_between, 100))
        elif accu == "sissors":
            screen.blit(sissors, dest=(
                margin + asset_width + space_between, 100))

        # black border on selected item
        if iter[0] == selected_item:
            points = [
                (x, y),
                (x + asset_width, y),
                (x + asset_width, y + asset_height),
                (x, y + asset_height),
            ]
            pygame.draw.lines(screen, black, closed=True,
                              points=points, width=10)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
