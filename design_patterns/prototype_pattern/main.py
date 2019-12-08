# -*- coding: utf-8 -*-
from prototype_pattern.Prototype import Prototype, Member


if __name__ == '__main__':
    member = Member('test clone')
    prototype = Prototype(member)
    prototype_clone = prototype.clone()
    prototype.get_member().set_name('test')

    print("----------------Prototype--------------------")
    print(prototype.get_member().get_name())
    print(prototype.get_member())
    print(prototype)

    print("----------------Prototype Clone--------------------")
    print(prototype_clone.get_member().get_name())
    print(prototype_clone.get_member())
    print(prototype_clone)
