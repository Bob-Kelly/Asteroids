from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from Shots import Shot
import pygame
import sys

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt = dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()

        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    print("Collision Detected!")
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()