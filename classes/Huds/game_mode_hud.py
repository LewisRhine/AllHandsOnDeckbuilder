from pygame.font import Font
from pygame.math import Vector2
from pygame.surface import SurfaceType

from classes.game_mode import GameMode


class GameModeHud:
    def __init__(self, hud_pos: Vector2):
        self.hud_pos = hud_pos

    def draw(self, screen: SurfaceType, game_mode: GameMode, action_mode_countdown: int):
        counter = ''
        if game_mode == GameMode.ACTION: counter = action_mode_countdown
        text_surf = Font(None, 50).render(f'Mode: {game_mode} {counter}', True, 'White')
        screen.blit(text_surf, self.hud_pos)
