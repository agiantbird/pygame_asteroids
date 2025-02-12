import pygame
from constants import *
from player import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20, 51)
            direction_one = self.velocity.rotate(random_angle)
            direction_two = self.velocity.rotate(random_angle * -1)

            smaller_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, smaller_radius)
            asteroid_one.velocity = direction_one * 1.2
            asteroid_two = Asteroid(self.position.x, self.position.y, smaller_radius)
            asteroid_two.velocity = direction_two * 1.2
            self.kill()
