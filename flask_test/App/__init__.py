# -*- coding: UTF-8 -*-

from flask import Blueprint

mainApp = Blueprint(__name__ + "_app", __name__, url_prefix='/Test')

from . import appTest
