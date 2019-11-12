# -*- coding: utf-8 -*-
from AbstractFactoryPattern.ThemeFactory.BrightThemeFactory import BrightThemeFactory
from AbstractFactoryPattern.ThemeFactory.DarkThemeFactory import DarkThemeFactory


if __name__ == '__main__':
    print('================亮主题================')
    brightThemeFactory = BrightThemeFactory()
    brightTheme = brightThemeFactory.createTheme()
    brightTheme.getFont().show()
    brightTheme.getColour().show()
    brightTheme.getIcon().show()
    print('================暗主题================')
    darkThemeFactory = DarkThemeFactory()
    darkTheme = darkThemeFactory.createTheme()
    darkTheme.getFont().show()
    darkTheme.getColour().show()
    darkTheme.getIcon().show()
