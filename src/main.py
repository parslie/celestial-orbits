import color
import random

import pygame
from pygame import Color, Vector2

from objects.celestial import CelestialObject


def generate_bg(size: tuple[int, int]) -> pygame.Surface:
    bg = pygame.Surface(size)
    bg.fill(color.BACKGROUND)

    random.seed(69)
    for i in range(420):
        x = round(random.random() * size[0])
        y = round(random.random() * size[1])
        bg.set_at((x, y), color.STAR)

    return bg


def main():
    pygame.init()
    pygame.display.set_caption('Physics Concepts')
    screen = pygame.display.set_mode((640, 480))

    game_objects = [
        CelestialObject(10, Vector2(0, 0), Vector2(0, 0), 10, Color(255, 255, 255))
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bg = generate_bg(screen.get_size())
        screen.blit(bg, (0, 0))

        for obj in game_objects:
            obj.pre_update(0)  # TODO: add better deltatime
        for obj in game_objects:
            obj.update(0)  # TODO: add better deltatime
            obj.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
