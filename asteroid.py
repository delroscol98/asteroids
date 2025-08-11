import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        image_path = "./images/asteroid.png"
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (self.radius * 2, self.radius * 2))
        image_center = image.get_rect()
        image_center.center = (self.position.x, self.position.y)

        screen.blit(image, image_center)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20, 50)
        sub_vec_1 = self.velocity.rotate(rand_angle)
        sub_vec_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_1.velocity = sub_vec_1 * 1.2

        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2.velocity = sub_vec_2 * 1.2
