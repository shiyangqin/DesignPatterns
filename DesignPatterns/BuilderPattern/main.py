# -*- coding: utf-8 -*-
from BuilderPattern.Builder.DellComputerBuilder import DellComputerBuilder
from BuilderPattern.Builder.HPComputerBuilder import HPComputerBuilder
from BuilderPattern.Director import ComputerDirector

if __name__ == '__main__':
    director = ComputerDirector()
    hp = HPComputerBuilder()
    dell = DellComputerBuilder()
    computer = None

    print('>>>>>>生产一台惠普电脑')
    director.setComputerBuilder(hp)
    director.constructComputer()
    computer = director.getComputer()

    print('>>>>>>生产一台戴尔电脑')
    director.setComputerBuilder(dell)
    director.constructComputer()
    computer = director.getComputer()
