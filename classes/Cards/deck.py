from classes.Cards.base_card import BaseCard
import random


class Deck:
    def __init__(self) -> None:
        self._deck = []

    def add_to_deck(self, new_card):
        if len(self._deck) < 50:
            self._deck.append(new_card)
        else:
            print("Deck is full")

    def shuffle_deck(self):
        random.shuffle(self._deck)

    def draw_card(self):
        print("drawing card")
        return self._deck.pop(-1)
