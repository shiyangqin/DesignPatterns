# -*- coding: utf-8 -*-
from abstract_factory_pattern.ThemeFactory.bright_theme_factory import BrightThemeFactory
from abstract_factory_pattern.ThemeFactory.dark_theme_factory import DarkThemeFactory


if __name__ == '__main__':
    print('================亮主题================')
    bright_theme_factory = BrightThemeFactory()
    bright_theme = bright_theme_factory.create_theme()
    bright_theme.get_font().show()
    bright_theme.get_colour().show()
    bright_theme.get_icon().show()
    print('================暗主题================')
    dark_theme_factory = DarkThemeFactory()
    dark_theme = dark_theme_factory.create_theme()
    dark_theme.get_font().show()
    dark_theme.get_colour().show()
    dark_theme.get_icon().show()
