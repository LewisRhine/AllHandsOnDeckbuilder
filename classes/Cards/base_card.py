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


class FireTorpedoes(BaseCard):
    def __init__(
        self,
        type=CardType.attack,
        cost_to_play=1,
        name="fire torpedoes!",
        effect_text="target targe that explosion and fire!",
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


fire_torpedoes = FireTorpedoes(
    # CardType.attack,
    # 1,
    # "fire torpedoes!",
    # "target targe that explosion and fire!",
)

fire_lasers = FireLasers(
    # CardType.attack,
    # 1,
    # "Fire Lasers!",
    # "Activate Laser attack for ONE round",
)

power_to_the_engines = PowerToTheEngines(
    # CardType.move,
    # 1,
    # "Power to the engines!",
    # "I am a leaf on the wind... Watch how I soar…!",
)

shields_up = ShieldsUp(
    # CardType.defense,
    # 1,
    # "Shields Up!!",
    # "Plus 5 to shields",
)

# print(fire_torpedoes.__dict__)
# print(fire_lasers.__dict__)
# print(power_to_the_engines.__dict__)
print(shields_up.__dict__)
