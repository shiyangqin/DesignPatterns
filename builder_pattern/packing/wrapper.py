# -*- coding: utf-8 -*-
"""
纸盒包装
"""
from builder_pattern.packing import Packing

class Wrapper(Packing):
    """
    纸盒包装
    """
    def pack(self):
        """纸盒包装"""
        return "Wrapper"
