import pytest
import pygame

import gui

def test_setup_gui():
    gui.setup_gui()
    assert pygame.get_init()