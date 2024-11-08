from constants import PLAYER_RADIUS
from circleshape import CircleShape

import pygame
from pygame import Vector2

class Player(CircleShape):
    """The player."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0

    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
