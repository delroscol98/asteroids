import pygame

from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.cooldown_timer = 0
        self.image = None
        self.image_center = None

    def spaceship(self):
        image_path = "./images/spaceship.png"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.image = pygame.transform.rotate(self.image, -self.rotation)
        
        self.image_center = self.image.get_rect()
        self.image_center.center = (self.position.x, self.position.y)
 
    def draw(self, screen):
        self.spaceship()
        screen.blit(self.image, self.image_center)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.cooldown_timer -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_TURN_SPEED * dt

    def shoot(self, dt):
        if self.cooldown_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
