import os
import pygame
from enum import Enum


class GameChoice(Enum):
    Rock = 0
    Paper = 1
    Sissors = 2

    def next(self):
        if self == GameChoice.Rock:
            return GameChoice.Paper
        elif self == GameChoice.Paper:
            return GameChoice.Sissors
        elif self == GameChoice.Sissors:
            return GameChoice.Rock

    def previous(self):
        if self == GameChoice.Rock:
            return GameChoice.Sissors
        elif self == GameChoice.Paper:
            return GameChoice.Rock
        elif self == GameChoice.Sissors:
            return GameChoice.Paper


def asset_loader(type):
    asset_file = ""
    if type == GameChoice.Rock:
        asset_file = "stone.png"
    elif type == GameChoice.Paper:
        asset_file = "paper.png"
    elif type == GameChoice.Sissors:
        asset_file = "sissors.png"

    return pygame.image.load(os.path.join("assets", asset_file))
