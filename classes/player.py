import pygame

from classes.ship import Ship


class Player(Ship):

    def __init__(self, x: int, y: int):
        self.image = pygame.image.load('assets/ships/Ship2/Ship2.png').convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        super().__init__(x, y, 1, 15)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: self.turn(-self.engines / 2)
        if keys[pygame.K_d]: self.turn(self.engines / 2)
        if keys[pygame.K_w]:
            self.accelerate(5)
        else:
            self.brake()
        if keys[pygame.K_s]: self.reverse(5)

    def update(self):
        self.player_input()
        super().update()
