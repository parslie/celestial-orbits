import math
from pygame import Vector2, Color

SCREEN_SIZE = Vector2(800)
METERS_PER_PIXEL = 10 ** 8.8
SPACE_SIZE = SCREEN_SIZE * METERS_PER_PIXEL

GRAV_CONSTANT = 6.674 * (10 ** -11)
PLANET_SIZE_FACTOR = 10 ** 3
SUN_SIZE_FACTOR = 20


def _calc_orbit_speed(central_mass, radius):
    return math.sqrt(GRAV_CONSTANT * central_mass / radius)


SUN_MASS = 1.989 * 10 ** 30
SUN_POSITION = SPACE_SIZE / 2
SUN_VELOCITY = Vector2()
SUN_RADIUS = 696340 * 10 ** 3 * SUN_SIZE_FACTOR
SUN_COLOR = Color(255, 255, 0)

MARS_DIST = 234.32 * 10 ** 9
MARS_MASS = 6.39 * 10 ** 23
MARS_POSITION = SUN_POSITION + Vector2(MARS_DIST, 0)
MARS_VELOCITY = Vector2(0, _calc_orbit_speed(SUN_MASS, MARS_DIST))
MARS_RADIUS = 3389.5 * 10 ** 3 * PLANET_SIZE_FACTOR
MARS_COLOR = Color(255, 64, 0)

EARTH_DIST = 147.24 * 10 ** 9
EARTH_MASS = 5.972 * 10 ** 24
EARTH_POSITION = SUN_POSITION + Vector2(EARTH_DIST, 0)
EARTH_VELOCITY = Vector2(0, _calc_orbit_speed(SUN_MASS, EARTH_DIST))
EARTH_RADIUS = 6371 * 10 ** 3 * PLANET_SIZE_FACTOR
EARTH_COLOR = Color(0, 0, 255)

VENUS_DIST = 107.87 * 10 ** 9
VENUS_MASS = 4.867 * 10 ** 24
VENUS_POSITION = SUN_POSITION + Vector2(VENUS_DIST, 0)
VENUS_VELOCITY = Vector2(0, _calc_orbit_speed(SUN_MASS, VENUS_DIST))
VENUS_RADIUS = 6051.8 * 10 ** 3 * PLANET_SIZE_FACTOR
VENUS_COLOR = Color(255, 148, 0)

MERCURY_DIST = 66.487 * 10 ** 9
MERCURY_MASS = 3.285 * 10 ** 23
MERCURY_POSITION = SUN_POSITION + Vector2(MERCURY_DIST, 0)
MERCURY_VELOCITY = Vector2(0, _calc_orbit_speed(SUN_MASS, MERCURY_DIST))
MERCURY_RADIUS = 2439.7 * 10 ** 3 * PLANET_SIZE_FACTOR
MERCURY_COLOR = Color(164, 164, 164)