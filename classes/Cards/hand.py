import base_card
import deck

# place holder for cards that have been played
class PlayedCards:
    def cards_to_play(card):
        pass


# place holder for discarded cards
class DiscardPile:
    def add_to_discard_pile(card):
        pass


class Hand:
    def __init__(self, discard_pile: DiscardPile, played_cards: PlayedCards) -> None:
        self._hand = []
        self.discard_pile = discard_pile

    def add_to_hand(self, new_card):
        self._hand.append(new_card)

    def discard_card(self, card):
        self._hand.remove(card)
        self.discard_pile.add_to_discard_pile(card)

    def play_card(self, card):
        self._hand.remove(card)
        self.discard_pile.add_to_discard_pile(card)
