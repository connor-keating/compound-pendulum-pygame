"""Module containing functions to setup the GUI for the app"""

import pygame

def setup_gui():
    pygame.init()
    pygame.display.set_mode([500, 500], pygame.FULLSCREEN)