from pygame import Vector2
from pygame.font import Font
from pygame.surface import SurfaceType

from classes.player import Player
from uitls import percentage


class PlayerShipStatus:
    def __init__(self, player_ship: Player, hud_pos: Vector2):
        self.hud_pos = hud_pos
        self._font = Font(None, 20)
        self.player_ship = player_ship

    def draw(self, screen: SurfaceType):
        hud_pos = Vector2(self.hud_pos)
        screen.blit(Font(None, 25).render('Ship status:', True, 'White'), hud_pos)

        hud_pos.y += 25
        hi = f'Hull Integrity: {self.player_ship.hull_integrity}'
        screen.blit(self._font.render(hi, True, 'White'), hud_pos)

        hud_pos.y += 20
        pa = f'Power Allotment: {percentage(self.player_ship.power_left, self.player_ship.power_allotment)}'
        screen.blit(self._font.render(pa, True, 'White'), hud_pos)

        hud_pos.y += 20
        pts = f'Power to Engines: {percentage(self.player_ship.engine_power, self.player_ship.power_allotment)}'
        screen.blit(self._font.render(pts, True, 'White'), hud_pos)

        hud_pos.y += 20
        pts = f'Power to Shields: {percentage(self.player_ship.shielding_power, self.player_ship.power_allotment)}'
        screen.blit(self._font.render(pts, True, 'White'), hud_pos)

        hud_pos.y += 20
        pts = f'Power to Weapons: {percentage(self.player_ship.weapon_power, self.player_ship.power_allotment)}'
        screen.blit(self._font.render(pts, True, 'White'), hud_pos)

        hud_pos.y += 20
        ls: str
        if self.player_ship.lasers_online and self.player_ship.power_to_lasers > 0:
            power_to_lasers = self.player_ship.power_to_lasers
            ls = f'Lasers: Online at {percentage(power_to_lasers, self.player_ship.weapon_power)} power'
        else:
            ls = 'Lasers: Offline'
        screen.blit(self._font.render(ls, True, 'White'), hud_pos)

        hud_pos.y += 20
        ts: str
        if self.player_ship.torpedo_online:
            ts = f'Torpedo: Online {self.player_ship.torpedo_loaded} ready'
        else:
            ts = 'Torpedo: Offline'
        screen.blit(self._font.render(ts, True, 'White'), hud_pos)
