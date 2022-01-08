from enum import Enum


class CardType(Enum):
    attack = 1
    move = 2
    defense = 3


class BaseCard:
    def __init__(self, type: CardType, cost_to_play: int, name: str, effect_text: str):
        self.type = type
        self.cost_to_play = cost_to_play
        self.name = name
        self.effect_text = effect_text

    def __str__(self) -> str:
        return self.name


class FireTorpedoes(BaseCard):
    def __init__(
        self,
        type=CardType.attack,
        cost_to_play=1,
        name="fire torpedoes!",
        effect_text="Target that explosion and fire!",
    ):
        super().__init__(type, cost_to_play, name, effect_text)


class FireLasers(BaseCard):
    def __init__(
        self,
        type=CardType.attack,
        cost_to_play=1,
        name="Fire Lasers!",
        effect_text="Activate Laser attack for ONE round",
    ):
        super().__init__(type, cost_to_play, name, effect_text)


class PowerToTheEngines(BaseCard):
    def __init__(
        self,
        type=CardType.move,
        cost_to_play=1,
        name="Power to the engines!",
        effect_text="I am a leaf on the wind... Watch how I soar…",
    ):
        super().__init__(type, cost_to_play, name, effect_text)


class ShieldsUp(BaseCard):
    def __init__(
        self,
        type=CardType.defense,
        cost_to_play=1,
        name="Shields Up!",
        effect_text="Plus 5 to shields",
    ):
        super().__init__(type, cost_to_play, name, effect_text)
