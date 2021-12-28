import pygame, sys

from pygame.sprite import GroupSingle

from classes.player import Player

pygame.init()
pygame.display.set_caption('All Hands on Deck(builder)')

screem_size = 1280, 720
screen = pygame.display.set_mode(screem_size)
background = pygame.surface.Surface(screem_size)
clock = pygame.time.Clock()

player = GroupSingle()
player.add(Player(1280 // 2, 720 // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(background, (0, 0))
    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)
