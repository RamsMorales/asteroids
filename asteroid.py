from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        random_direction = self.velocity.rotate(angle)
        split_direction = -random_direction

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        daughter_asteroid_left = Asteroid(self.position[0], self.position[1], new_radius)
        daughter_asteroid_right = Asteroid(self.position[0], self.position[1], new_radius)

        daughter_asteroid_left.velocity = 1.2 * random_direction
        daughter_asteroid_right.velocity = 1.2 * split_direction

