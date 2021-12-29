import pygame

from classes.ship import Ship


class Player(Ship):
    def __init__(self, x: int, y: int):
        self.image = pygame.image.load('assets/ships/Ship2/Ship2.png').convert_alpha()
        # the ship class only works with images that are pointing up.
        # Since our ship asset point to the right we need to rotate the image by 90 to start off
        self.image = pygame.transform.rotate(self.image, 90)
        super().__init__(x, y, power_allotment=3, hull_integrity=100)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.turn_left()
        if keys[pygame.K_d]: self.turn_right()
        if keys[pygame.K_w]:
            self.accelerate()
        elif keys[pygame.K_s]:
            self.reverse()
        else:
            self.brake()

    def update(self):
        self.player_input()
        if self.weapon_power > 0:
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(pygame.cursors.tri_left)
        super().update()
