import pygame
from pygame import Color, Vector2

from .rigidbody import RigidBody


class CelestialObject(RigidBody):
    def __init__(self, mass: float, position: Vector2, velocity: Vector2, radius: int, color: Color):
        super().__init__(mass, position, velocity)
        self.radius = radius
        self.color = color

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius)