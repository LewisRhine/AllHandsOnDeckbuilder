import pygame, sys
from pygame.math import Vector2

from pygame.sprite import GroupSingle

from classes.Huds.game_mode_hud import GameModeHud
from classes.Huds.player_ship_status_hud import PlayerShipStatus
from classes.game_mode import GameMode
from classes.player import Player

pygame.init()
pygame.display.set_caption('All Hands on Deck(builder)')

screem_size = 1280, 720
screen = pygame.display.set_mode(screem_size)
background = pygame.surface.Surface(screem_size)
clock = pygame.time.Clock()

player_ship = Player(1280 // 2, 720 // 2)
player = GroupSingle()
player.add(player_ship)
player_ship_status_hud = PlayerShipStatus(player_ship, Vector2(50, 50))

ACTION_MODE_COUNTDOWN_START = 250
action_mode_countdown = ACTION_MODE_COUNTDOWN_START

game_mode: GameMode = GameMode.FREE_MOVE
game_mode_hud = GameModeHud(Vector2(500, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1: player_ship.power_to_engines(1)
            if event.key == pygame.K_2: player_ship.power_to_shielding(1)
            if event.key == pygame.K_3: player_ship.power_to_weapons(1)
            if event.key == pygame.K_0: player_ship.reset_power()
            if event.key == pygame.K_p: game_mode = GameMode.ACTION

    screen.blit(background, (0, 0))
    player.draw(screen)
    player.update()
    player_ship_status_hud.draw(screen)
    player_ship.render_shield(screen)
    game_mode_hud.draw(screen, game_mode, action_mode_countdown)
    pygame.display.update()
    clock.tick(60)
