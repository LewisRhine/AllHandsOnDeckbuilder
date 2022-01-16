import pygame, sys

from pygame.sprite import GroupSingle

from classes.player import Player

from classes.Cards.deck import Deck
from classes.Cards.base_card import BaseCard
import classes.Cards.hand

pygame.init()
pygame.display.set_caption("All Hands on Deck(builder)")

screem_size = 1280, 720
screen = pygame.display.set_mode(screem_size)
background = pygame.surface.Surface(screem_size)
clock = pygame.time.Clock()

player = GroupSingle()
player.add(Player(1280 // 2, 720 // 2))

player_deck = Deck()
player_deck.add_to_deck(classes.Cards.base_card.FireLasers())
player_deck.add_to_deck(classes.Cards.base_card.FireLasers())
player_deck.add_to_deck(classes.Cards.base_card.FireLasers())
player_deck.add_to_deck(classes.Cards.base_card.FireTorpedoes())
player_deck.add_to_deck(classes.Cards.base_card.FireTorpedoes())
player_deck.add_to_deck(classes.Cards.base_card.PowerToTheEngines())
player_deck.add_to_deck(classes.Cards.base_card.PowerToTheEngines())
player_deck.add_to_deck(classes.Cards.base_card.ShieldsUp())
player_deck.add_to_deck(classes.Cards.base_card.ShieldsUp())
player_deck.shuffle_deck()


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
