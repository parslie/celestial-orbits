from pygame import Color, Vector2

from .gameobject import GameObject
from constants import GRAV_CONSTANT


class RigidBody(GameObject):
    def __init__(self, mass: float, position: Vector2, velocity: Vector2):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.force = Vector2(0, 0)

    def force_to(self, other):
        if not isinstance(other, RigidBody):
            return

        displacement = other.position - self.position
        force = GRAV_CONSTANT * self.mass * other.mass / displacement.magnitude_squared()
        return force * displacement.normalize()

    def pre_update(self, dt, *others) -> None:
        self.force = Vector2(0, 10)
        for other in others:
            if isinstance(other, RigidBody):
                self.force += self.force_to(other)

    def update(self, dt, *others) -> None:
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt