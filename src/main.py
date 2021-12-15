import random
import math

import pygame
from pygame import Surface, Vector2, Color

from objects.celestial import CelestialObject
from constants import *


def generate_bg(size: Vector2) -> Surface:
    bg = Surface(size)
    bg.fill(Color(6, 0, 18))

    random.seed(69)
    for i in range(420):
        x = round(random.random() * size.x)
        y = round(random.random() * size.y)
        bg.set_at((x, y), Color(128, 128, 138))

    return bg


def init_celestial_bodies() -> set:
    bodies = set()

    bodies.add(CelestialObject(
        SUN_MASS,
        SUN_POSITION,
        SUN_VELOCITY,
        SUN_RADIUS,
        SUN_COLOR
    ))

    bodies.add(CelestialObject(
        MERCURY_MASS,
        MERCURY_POSITION,
        MERCURY_VELOCITY,
        MERCURY_RADIUS,
        MERCURY_COLOR
    ))

    bodies.add(CelestialObject(
        VENUS_MASS,
        VENUS_POSITION,
        VENUS_VELOCITY,
        VENUS_RADIUS,
        VENUS_COLOR
    ))

    bodies.add(CelestialObject(
        EARTH_MASS,
        EARTH_POSITION,
        EARTH_VELOCITY,
        EARTH_RADIUS,
        EARTH_COLOR
    ))

    bodies.add(CelestialObject(
        MARS_MASS,
        MARS_POSITION,
        MARS_VELOCITY,
        MARS_RADIUS,
        MARS_COLOR
    ))

    return bodies


def main():
    pygame.init()
    pygame.display.set_caption('Celestial Orbits')
    screen = pygame.display.set_mode(SCREEN_SIZE)

    game_objects = init_celestial_bodies()

    clock = pygame.time.Clock()
    running = True
    while running:
        delta_time = 60 * 60 * 24  # Every frame simulates a day

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(generate_bg(SCREEN_SIZE), Vector2())

        for obj in game_objects:
            others = game_objects - set([obj])
            obj.pre_update(delta_time, *others)
        for obj in game_objects:
            others = game_objects - set([obj])
            obj.update(delta_time, *others)
            obj.draw(screen)
    
        pygame.display.flip()
        clock.tick(60)  # Every second simulates 60 days


if __name__ == '__main__':
    main()
