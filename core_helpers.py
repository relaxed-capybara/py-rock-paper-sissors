import os
import pygame
from core_types import GameChoice
import random


def asset_loader(type):
    asset_file = ""
    if type == GameChoice.Rock:
        asset_file = "stone.png"
    elif type == GameChoice.Paper:
        asset_file = "paper.png"
    elif type == GameChoice.Sissors:
        asset_file = "sissors.png"

    return pygame.image.load(os.path.join("assets", asset_file))


def pick_cpu_choice():
    all = all_choices()

    cpu_choice = random.randrange(0, len(all))
    return all[cpu_choice]


def all_choices():
    return [GameChoice.Rock, GameChoice.Paper, GameChoice.Sissors]
