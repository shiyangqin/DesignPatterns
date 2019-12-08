# -*- coding: utf-8 -*-
import random
from flyweight_pattern.shape import ShapeFactory

color = ("Red", "Green", "Blue", "White", "Black")

def get_random_colors():
    return color[random.randint(0, len(color) - 1)]


def get_random_x():
    return random.randint(0, 100)


def get_random_y():
    return random.randint(0, 100)


def get_random_radius():
    return random.randint(0, 100)


if __name__ == '__main__':
    for i in range(20):
        circle = ShapeFactory.get_circle(get_random_colors())
        circle.set_x(get_random_x())
        circle.set_y(get_random_y())
        circle.set_radius(get_random_radius())
        circle.draw()
