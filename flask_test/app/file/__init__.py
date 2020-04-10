# -*- coding: UTF-8 -*-
from flask import Blueprint

file_app = Blueprint(__name__ + "_app", __name__, url_prefix='/file')

from . import file
