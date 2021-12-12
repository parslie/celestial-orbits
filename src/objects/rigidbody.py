from pygame import Color, Vector2

from .gameobject import GameObject


class RigidBody(GameObject):
    def __init__(self, mass: float, position: Vector2, velocity: Vector2):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector2(0, 0)

    def pre_update(self, dt, *others) -> None:
        for other in others:
            if isinstance(other, RigidBody):
                print('asd')

    def update(self, dt, *others) -> None:
        pass