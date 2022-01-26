import pygame, sys

from pygame.sprite import GroupSingle

from classes.player import Player

from classes.Cards.deck import Deck
from classes.Cards.base_card import (
    BaseCard,
    FireTorpedoes,
    FireLasers,
    PowerToTheEngines,
    ShieldsUp,
)
from classes.Cards.hand import (
    Hand,
    DiscardPile,
)

pygame.init()
pygame.display.set_caption("All Hands on Deck(builder)")

screem_size = 1280, 720
screen = pygame.display.set_mode(screem_size)
background = pygame.surface.Surface(screem_size)
clock = pygame.time.Clock()

player = GroupSingle()
player.add(Player(1280 // 2, 720 // 2))

# adding player deck and building with predetermined set of cards
player_deck = Deck()
player_deck.add_to_deck(FireLasers())
player_deck.add_to_deck(FireLasers())
player_deck.add_to_deck(FireLasers())
player_deck.add_to_deck(FireTorpedoes())
player_deck.add_to_deck(FireTorpedoes())
# player_deck.add_to_deck(PowerToTheEngines())
# player_deck.add_to_deck(PowerToTheEngines())
# player_deck.add_to_deck(ShieldsUp())
# player_deck.add_to_deck(ShieldsUp())
# player_deck.add_to_deck(ShieldsUp())
# player_deck.shuffle_deck()
# creating player hand and discard pile and fillinf hand with last 5 cards from player's deck
player_discard_pile = DiscardPile()
player_hand = Hand(
    discard_pile=player_discard_pile,
)
# player_hand.add_to_hand(player_deck.draw_card())
# player_hand.add_to_hand(player_deck.draw_card())
# player_hand.add_to_hand(player_deck.draw_card())
# player_hand.add_to_hand(player_deck.draw_card())
# player_hand.add_to_hand(player_deck.draw_card())

print(f" first hand {player_hand._hand}")

# a function in main that will be called when a new round of card mode starts.
#   the function discarded any cards in the player's hand then draw five new cards.
#   If deck does not contain 5 cards, cards are pulled from discardpile and suffled


def new_card_round():
    global player_hand
    global player_deck
    player_hand.discard_hand()
    print(len(player_hand._hand))
    # Checks for 5 cards in deck if there are less than 5
    #   the discard pile is moived to deck and deck is resuffled
    if len(player_deck._deck) < 5:
        player_discard_pile.send_to_deck()
        player_deck._deck = player_discard_pile._return_pile
    while len(player_hand._hand) < 5:
        player_hand.add_to_hand(player_deck.draw_card())

        #     player_deck.add_to_deck(player_discard_pile._discard_pile[0])
        #     player_deck.shuffle_deck()
        #     print("refilled deck")
        # else:
        #     player_discard_pile.add_to_discard_pile(player_hand)
        #     player_hand._hand = []
        #     player_deck.shuffle_deck()
        #     player_hand.add_to_hand(player_deck.draw_card())
        #     player_hand.add_to_hand(player_deck.draw_card())
        #     player_hand.add_to_hand(player_deck.draw_card())
        #     player_hand.add_to_hand(player_deck.draw_card())
        #     player_hand.add_to_hand(player_deck.draw_card())

    print(f" second hand {player_hand._hand}")


new_card_round()
new_card_round()
new_card_round()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, (0, 0))
    player.draw(screen)
    player.update()

    # player_deck.add_to_deck(classes.Cards.base_card.FireLasers())
    # print(player_deck)

    pygame.display.update()
    clock.tick(60)
