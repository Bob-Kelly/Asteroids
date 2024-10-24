import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x_or_pos, y=None, radius=None, velocity=None):
        if y is None:
            position = pygame.Vector2(x_or_pos)
            super().__init__(position.x, position.y, radius)
            self.position = position
            self.velocity = radius if radius else pygame.Vector2(0, 0)
        else:
            super().__init__(x_or_pos, y, radius)
            self.position = pygame.Vector2(x_or_pos, y)
            self.velocity = velocity if velocity else pygame.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        print("Splitting Asteroid!")
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        print(f"Creating new asteroid with radius {new_radius}")
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid1.velocity = vel1
        asteroid2.velocity = vel2

        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)
                

