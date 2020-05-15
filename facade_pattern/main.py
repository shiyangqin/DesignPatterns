# -*- coding: utf-8 -*-
from facade_pattern.shape import ShapeMaker


if __name__ == '__main__':
    shape_maker = ShapeMaker()
    shape_maker.draw_circle()
    shape_maker.draw_rectangle()
    shape_maker.draw_square()
