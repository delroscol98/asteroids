# this allows us to use code from
# the open-source pygame libary
# throughout this file
import pygame
import sys

# import everything from the module
# constants.py into the current file
from constants import *

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Shot.containers = (updatable, drawable, shots)
    
    dt = 0

    score_value = 0
    font = pygame.font.Font("freesansbold.ttf", 32)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over! Your score was {int(score_value)}")
                sys.exit(0)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    score_value += 1
            

        pygame.Surface.fill(screen, (0, 0, 0))

        score_text = font.render(f"Score: {int(score_value)}", True, (255, 255, 255))
        
        screen.blit(score_text, (10, 10))

        for el in drawable:
            el.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

# this line ensures the main() function
# is only called when this file is
# run directly; it won't run if it's 
# imported as a module. It's considered the
# "pythonic" way tostructure an executable
# program in Python
if __name__ == "__main__":
   main()
