# -*- coding: utf-8 -*-
from FacadePattern.Shape import ShapeMaker


if __name__ == '__main__':
    shapeMaker = ShapeMaker()
    shapeMaker.drawCircle()
    shapeMaker.drawRectangle()
    shapeMaker.drawSquare()