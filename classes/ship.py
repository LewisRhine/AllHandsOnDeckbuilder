import math, pygame

from pygame.surface import SurfaceType

""" https://stackoverflow.com/questions/62240557/how-could-i-make-a-basic-car-physics-in-pygame """


class Ship(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, power_allotment: int, hull_integrity: int, rotations: int = 360):
        super().__init__()
        self._hull_integrity: int = hull_integrity
        self._power_allotment: int = power_allotment
        self._power_left: int = power_allotment
        self._engine_power: int = 0
        self._shielding_power: int = 0
        self._weapon_power: int = 0
        self.lasers_online: bool = False
        self.power_to_lasers: int = 0
        self.torpedo_online: bool = False
        self.torpedo_loaded: int = 0
        self._accelerating: bool = False
        self._reversing: bool = False
        self._rot_img = []
        self._min_angle = (360 / rotations)
        for i in range(rotations):
            rotated_image = pygame.transform.rotozoom(self.image, 360 - 90 - (i * self._min_angle), 1)
            self._rot_img.append(rotated_image)
        self._min_angle = math.radians(self._min_angle)
        self.image = self._rot_img[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._heading = 0
        self._speed = 0
        self._velocity = pygame.math.Vector2(0, 0)
        self._position = pygame.math.Vector2(x, y)

    @property
    def hull_integrity(self) -> int:
        return self._hull_integrity

    @hull_integrity.setter
    def hull_integrity(self, value: int):
        self._hull_integrity -= value
        if self._hull_integrity <= 0:
            print(f'ship {self.__class__.__name__} destroyed')
            self.kill()

    @property
    def power_allotment(self):
        return self._power_allotment

    # ----------------------------------------------------
    # these are read only props because we want things outside this class to only be able to use the "power_to" method
    # to set them. That way the class has control over checking that there is enough left in power_allotment
    # and subtracting it when putting power into other systems
    @property
    def power_left(self) -> int:
        return self._power_left

    @property
    def engine_power(self):
        return self._engine_power

    @property
    def shielding_power(self):
        return self._shielding_power

    @property
    def weapon_power(self):
        return self._weapon_power

    # ---------------------------------------------------

    def power_to_shielding(self, amount: int):
        if amount > self.power_left: return
        self._shielding_power += amount
        self._power_left -= amount

    def power_to_engines(self, amount: int):
        if amount > self.power_left: return
        self._engine_power += amount
        self._power_left -= amount

    def power_to_weapons(self, amount: int):
        if amount > self.power_left: return
        self._weapon_power += amount
        self._power_left -= amount

    def reset_power(self):
        self._power_left = self._power_allotment
        self._engine_power = 0
        self._shielding_power = 0
        self._weapon_power = 0

    def turn_left(self):
        self.__turn(-self._engine_power / 2)

    def turn_right(self):
        self.__turn(self._engine_power / 2)

    def __turn(self, angle_degrees: float):
        self._heading += math.radians(angle_degrees)
        image_index = int(self._heading / self._min_angle) % len(self._rot_img)
        if self.image != self._rot_img[image_index]:
            x, y = self.rect.center
            self.image = self._rot_img[image_index]
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    def accelerate(self):
        self._accelerating = True
        if not self._speed >= self._engine_power:
            self._speed += 0.05

    def reverse(self):
        self._reversing = True
        if not self._speed <= -self._engine_power:
            self._speed -= 0.05

    def brake(self):
        self._accelerating = False
        self._reversing = False

    def update(self):
        self._velocity.from_polar((self._speed, math.degrees(self._heading)))
        self._position += self._velocity
        self.rect.center = (round(self._position[0]), round(self._position[1]))
        if self._speed > 0 and not self._accelerating:
            self._speed -= 0.05
        if self._speed < 0 and not self._reversing:
            self._speed += 0.05

    def render_shield(self, screen: SurfaceType):
        if self._shielding_power <= 0: return

        target_rect = pygame.Rect(self._position, (0, 0)).inflate((100 * 2, 100 * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(
            shape_surf, (0, 0, 205, 30 + self._shielding_power * 10),
            (100, 100),
            50 + self._shielding_power * 10)
        screen.blit(shape_surf, target_rect)
