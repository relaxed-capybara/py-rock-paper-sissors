# Example file showing a basic pygame "game loop"
import pygame
import os
import random

from core_types import GameChoice, asset_loader
from turning_things_into_functions import fadingEfect, activator, handle_fade, change_icon, draw_icon


class GameState:
    def __init__(self):
        self.selected_item = GameChoice.Rock
        self.running = True
        self.timer = 0
        self.fade_alpha = 255
        self.fading_active = False
        self.index_ = None
        self.lovly_sissors = asset_loader(GameChoice.Sissors)
        self.lovly_paper = asset_loader(GameChoice.Paper)
        self.lovly_stone = asset_loader(GameChoice.Rock)
        self.icons = [
            self.lovly_stone,
            self.lovly_paper,
            self.lovly_sissors,
        ]
        self.locked = False
        self.enemy_alpha = 255
        self.accu = "rock"
        self.timerAL = 0
        self.screen_width = 1000
        self.screen_height = 1000
        self.asset_width = 256
        self.asset_height = 256
        self.space_between = 64
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.margin = (screen_width - (asset_width *
                       3 + space_between * 2)) / 2
        self.sissors = pygame.image.load(os.path.join("assets", "sissors.png"))
        self.paper = pygame.image.load(os.path.join("assets", "paper.png"))
        self.stone = pygame.image.load(os.path.join("assets", "stone.png"))
        self.font = font
        self.wins = 0
        self.loses = 0
        self.ties = 0

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
font = pygame.font.SysFont("Arail", 10)
# Setup
clock = pygame.time.Clock()

# In-game state
state = GameState()

while state.running:
    deltaTime = clock.get_time() / 1000

    # closing the screan
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state.running = False

            # chosing part
            if not state.locked:
                if event.key == pygame.K_RIGHT:
                    state.selected_item = state.selected_item.next()
                elif event.key == pygame.K_LEFT:
                    state.selected_item = state.selected_item.previous()

            # if state.selected_item > 2:
            #     state.selected_item = 0
            # elif state.selected_item < 0:
            #     state.selected_item = 2

            # handling fading
            if not state.locked and event.key == pygame.K_SPACE:
                if state.selected_item.value == 0:
                    activator(0, state, event)
                elif state.selected_item.value == 1:
                    activator(1, state, event)
                elif state.selected_item.value == 2:
                    activator(2, state, event)

    # fading the icons and orange
    handle_fade(state)

    handle_fade(state)

    handle_fade(state)

    state.screen.fill("grey")

    state.timerAL += 1 / 60
    if state.timerAL >= 1 / 3:
        change_icon(state)

    # RENDER YOUR GAME HERE
    for iter in enumerate(state.icons):
        x = state.margin + (asset_width + space_between) * iter[0]
        y = (screen_height - asset_height) - 150

        # create fading orange surface with alpha
        # wtf
        orange_surface = pygame.Surface(
            (asset_width, asset_height), pygame.SRCALPHA)
        orange_surface.fill((orange.r, orange.g, orange.b, state.fade_alpha))
        state.screen.blit(orange_surface, (x, y))

        # blit icons as before
        state.screen.blit(iter[1], dest=(x, y))

        # second static orange rect (unchanged)
        pygame.draw.rect(state.screen, orange, pygame.Rect(
            (state.margin + asset_width + space_between, 100), (asset_width, asset_height)))

        draw_icon(state)
        # black border on selected item
        if iter[0] == state.selected_item.value:
            points = [
                (x, y),
                (x + asset_width, y),
                (x + asset_width, y + asset_height),
                (x, y + asset_height),
            ]
            pygame.draw.lines(state.screen, black, closed=True,
                              points=points, width=10)
        # scoring

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
