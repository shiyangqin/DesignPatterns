# -*- coding: utf-8 -*-
from PrototypePattern.Prototype import Prototype, Member


if __name__ == '__main__':
    member = Member('test clone')
    prototype = Prototype(member)
    prototypeClone = prototype.clone()
    prototype.getMember().setName('test')

    print("----------------Prototype--------------------")
    print(prototype.getMember().getName())
    print(prototype.getMember())
    print(prototype)

    print("----------------Prototype Clone--------------------")
    print(prototypeClone.getMember().getName())
    print(prototypeClone.getMember())
    print(prototypeClone)
