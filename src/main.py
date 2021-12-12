import random
import time
import math

import pygame
from pygame import Surface, Vector2, Color

from objects.celestial import CelestialObject
from objects.rigidbody import GRAV_CONSTANT


def generate_bg(size: Vector2) -> Surface:
    bg = Surface(size)
    bg.fill(Color(6, 0, 18))

    random.seed(69)
    for i in range(420):
        x = round(random.random() * size.x)
        y = round(random.random() * size.y)
        bg.set_at((x, y), Color(255, 255, 255))

    return bg


def main():
    pygame.init()
    pygame.display.set_caption('Physics Concepts')
    screen_size = Vector2(640, 640)
    screen = pygame.display.set_mode(screen_size, pygame.NOFRAME)

    game_objects = set()

    sun_mass = 1.989 * 10 ** 30
    game_objects.add(CelestialObject(
        sun_mass,
        screen_size / 2,
        Vector2(),
        16,
        Color(255, 255, 0)
    ))

    earth_dist = 200
    earth_speed = math.sqrt(GRAV_CONSTANT * sun_mass / earth_dist)
    game_objects.add(CelestialObject(
        5.972 * 10 ** 24,
        screen_size / 2 + Vector2(earth_dist, 0),
        Vector2(0, earth_speed),
        6.5,
        Color(0, 0, 255)
    ))

    venus_dist = earth_dist * (107.92 / 147.28)
    venus_speed = math.sqrt(GRAV_CONSTANT * sun_mass / venus_dist)
    game_objects.add(CelestialObject(
        4.867 * 10 ** 24,
        screen_size / 2 + Vector2(venus_dist, 0),
        Vector2(0, venus_speed),
        6,
        Color(255, 148, 0)
    ))

    mercury_dist = earth_dist * (57.91 / 147.28)
    mercury_speed = math.sqrt(GRAV_CONSTANT * sun_mass / mercury_dist)
    game_objects.add(CelestialObject(
        3.285 * 10 ** 23,
        screen_size / 2 + Vector2(mercury_dist, 0),
        Vector2(0, mercury_speed),
        2.5,
        Color(164, 164, 164)
    ))

    mars_dist = earth_dist * (227.9 / 147.28)
    mars_speed = math.sqrt(GRAV_CONSTANT * sun_mass / mars_dist)
    game_objects.add(CelestialObject(
        6.39 * 10 ** 23,
        screen_size / 2 + Vector2(mars_dist, 0),
        Vector2(0, mars_speed),
        3.5,
        Color(255, 64, 0)
    ))

    running = True
    prev_time = time.perf_counter()
    while running:
        curr_time = time.perf_counter()
        delta_time = (curr_time - prev_time) / 4000000  # Slow down time significantly to be able to see orbit
        prev_time = curr_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = generate_bg(screen_size)
        screen.blit(bg, Vector2())

        for obj in game_objects:
            others = game_objects - set([obj])
            obj.pre_update(delta_time, *others)
        for obj in game_objects:
            others = game_objects - set([obj])
            obj.update(delta_time, *others)
            obj.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
