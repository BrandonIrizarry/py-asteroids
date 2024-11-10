import pygame
from abc import ABC, abstractmethod

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):
    """Base class for game objects."""
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, circle_shape):
        distance = self.position.distance_to(circle_shape.position)

        return distance <= self.radius + circle_shape.radius

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, dt):
        pass
