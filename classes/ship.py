import math, pygame

""" https://stackoverflow.com/questions/62240557/how-could-i-make-a-basic-car-physics-in-pygame """


class Ship(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, engines: int, shielding: int, rotations: int = 360):
        super().__init__()
        self.engines = engines
        self.shielding = shielding
        self.rot_img = []
        self.min_angle = (360 / rotations)
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(self.image, 360 - 90 - (i * self.min_angle), 1)
            self.rot_img.append(rotated_image)
        self.min_angle = math.radians(self.min_angle)
        self.image = self.rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.heading = 0
        self.speed = 0
        self.velocity = pygame.math.Vector2(0, 0)
        self.position = pygame.math.Vector2(x, y)

    def turn(self, angle_degrees: float):
        self.heading += math.radians(angle_degrees)
        image_index = int(self.heading / self.min_angle) % len(self.rot_img)
        if self.image != self.rot_img[image_index]:
            x, y = self.rect.center
            self.image = self.rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def accelerate(self, amount: int):
        if amount > self.engines: amount = self.engines
        self.speed = amount

    def reverse(self, amount: int):
        if amount > self.engines: amount = self.engines
        self.speed = -amount

    def brake(self):
        self.speed = 0

    def update(self):
        self.velocity.from_polar((self.speed, math.degrees(self.heading)))
        self.position += self.velocity
        self.rect.center = (round(self.position[0]), round(self.position[1]))
