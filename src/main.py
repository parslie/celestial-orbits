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


def get_mouse_pos() -> Vector2:
    mouse_pos = pygame.mouse.get_pos()
    return Vector2(mouse_pos[0], mouse_pos[1]) * METERS_PER_PIXEL


def main():
    pygame.init()
    pygame.display.set_caption('Celestial Orbits')
    screen = pygame.display.set_mode(SCREEN_SIZE)

    game_objects = init_celestial_bodies()
    game_object_bin = set()

    is_creating_body = False
    new_body_position = Vector2()
    new_body_velocity = Vector2()

    clock = pygame.time.Clock()
    running = True
    while running:
        delta_time = 60 * 60 * 24  # Every frame simulates a day
        fps = 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                is_creating_body = True
                new_body_position = get_mouse_pos()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                is_creating_body = False
                new_body_velocity = (get_mouse_pos() - new_body_position) / (delta_time * fps)
                game_objects.add(CelestialObject(
                    EARTH_MASS,
                    new_body_position,
                    new_body_velocity,
                    EARTH_RADIUS,
                    EARTH_COLOR
                ))

        screen.blit(generate_bg(SCREEN_SIZE), Vector2())
        
        for obj in game_objects:
            others = game_objects - set([obj])
            obj.pre_update(delta_time, *others)
        for obj in game_objects:
            others = game_objects - set([obj])
            obj.update(delta_time, *others)
            try:
                obj.draw(screen)
            except OverflowError:
                game_object_bin.add(obj)
    
        game_objects -= game_object_bin
        game_object_bin.clear()

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    main()
