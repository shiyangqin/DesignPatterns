# -*- coding: utf-8 -*-
import random
from FlyweightPattern.Shape import ShapeFactory

color = ("Red", "Green", "Blue", "White", "Black")

def getRandomColors():
    return color[random.randint(0, len(color) - 1)]


def getRandomX():
    return random.randint(0, 100)


def getRandomY():
    return random.randint(0, 100)


def getRandomRadius():
    return random.randint(0, 100)


if __name__ == '__main__':
    for i in range(20):
        circle = ShapeFactory.getCircle(getRandomColors())
        circle.setX(getRandomX())
        circle.setY(getRandomY())
        circle.setRadius(getRandomRadius())
        circle.draw()
