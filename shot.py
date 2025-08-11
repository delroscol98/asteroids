import pygame

from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.image = pygame.image.load("./images/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius * 5, self.radius * 5))
        self.image = pygame.transform.rotate(self.image, -rotation)

    def draw(self, screen):
        image_center = self.image.get_rect()
        image_center.center = (self.position.x, self.position.y)

        screen.blit(self.image, image_center)

    def update(self, dt):
        self.position += self.velocity * dt
