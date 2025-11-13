import os
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


class GameResult(Enum):
    Tie = 0
    HumanWin = 1
    HumanLost = 2
