import pygame
from pygame import Color, Vector2, gfxdraw

from .rigidbody import RigidBody
from constants import METERS_PER_PIXEL


class CelestialObject(RigidBody):
    def __init__(self, mass: float, position: Vector2, velocity: Vector2, radius: int, color: Color):
        super().__init__(mass, position, velocity)
        self.radius = radius
        self.color = color

    def draw(self, screen) -> None:
        gfxdraw.aacircle(
            screen, 
            int(self.position.x / METERS_PER_PIXEL),
            int(self.position.y / METERS_PER_PIXEL),
            int(self.radius / METERS_PER_PIXEL),
            self.color
        )
        gfxdraw.filled_circle(
            screen, 
            int(self.position.x / METERS_PER_PIXEL),
            int(self.position.y / METERS_PER_PIXEL),
            int(self.radius / METERS_PER_PIXEL),
            self.color
        )