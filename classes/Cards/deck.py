import base_card
import random


class Deck:
    def __init__(self) -> None:
        self._deck = []

    def add_to_deck(self, new_card):
        if len(self._deck) < 50:
            self._deck.append(new_card)
        else:
            print("Deck is full")

        # print(f" {len(self._deck)} {self._deck}")

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def draw_card(self):
        return self._deck.pop(-1)


# d = Deck()
# d.add_to_deck(base_card.FireTorpedoes())
# d.add_to_deck(base_card.FireLasers())
# d.add_to_deck(base_card.PowerToTheEngines())
# d.add_to_deck(base_card.ShieldsUp())
# print(d._deck[0].cost_to_play)
# print(f" {len(d._deck)} {d._deck}")
# d.shuffle_deck()
# print(f"deck: {d._deck}")
# print(d.draw_card())
# print(f"deck: {d._deck}")
