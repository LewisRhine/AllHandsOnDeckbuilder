import math, pygame

""" https://stackoverflow.com/questions/62240557/how-could-i-make-a-basic-car-physics-in-pygame """


class Ship(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, max_engine_power: int, max_shielding_power: int, rotations: int = 360):
        super().__init__()
        self.max_engine_power = max_engine_power
        self.current_engine_power = self.max_engine_power
        self.max_shielding_power = 0
        self.current_shielding_power = max_shielding_power
        self.accelerating: bool = False
        self.reversing: bool = False
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

    def turn_left(self):
        self.turn(-self.current_engine_power / 2)

    def turn_right(self):
        self.turn(self.current_engine_power / 2)

    def turn(self, angle_degrees: float):
        self.heading += math.radians(angle_degrees)
        image_index = int(self.heading / self.min_angle) % len(self.rot_img)
        if self.image != self.rot_img[image_index]:
            x, y = self.rect.center
            self.image = self.rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def accelerate(self):
        self.accelerating = True
        if not self.speed >= self.current_engine_power:
            self.speed += 0.05

    def reverse(self):
        self.reversing = True
        if not self.speed <= -self.current_engine_power:
            self.speed -= 0.05

    def brake(self):
        self.accelerating = False
        self.reversing = False

    def update(self):
        self.velocity.from_polar((self.speed, math.degrees(self.heading)))
        self.position += self.velocity
        self.rect.center = (round(self.position[0]), round(self.position[1]))
        if self.speed > 0 and not self.accelerating:
            self.speed -= 0.05
        if self.speed < 0 and not self.reversing:
            self.speed += 0.05
