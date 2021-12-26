from enum import Enum
import enum


class Type(enum):
    attack = 1
    move = 2
    defense = 3


class BaseCard:
    def __init__(self, type, cost_to_play, name, effect_text):
        self.type = Type
        self.cost_to_play = cost_to_play
        self.name = name
        self.effect_text = effect_text


card_1 = BaseCard(1, 200, "fire torpedoes!", "target targe that explosion and fire!")

print(card_1.type)
