from enum import Enum


class GameMode(Enum):
    FREE_MOVE = 'Free move'
    CARD = 'Card'
    ACTION = 'Action'

    def __str__(self):
        return self.value
