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

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self, dt):
        pass
