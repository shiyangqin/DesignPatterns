# -*- coding: UTF-8 -*-

from flask import Blueprint

main_app = Blueprint(__name__ + "_app", __name__)

from . import test
