# -*- coding: utf-8 -*-
from Abstract_Factory_Pattern.ThemeFactory.BrightThemeFactory import BrightThemeFactory
from Abstract_Factory_Pattern.ThemeFactory.DarkThemeFactory import DarkThemeFactory


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
