"""
Main driver file
    Responsible for handling user input
    displaying the current GameState Object
"""

import pygame
import ChessEngine

WIDTH = HEIGHT = 512    # 400 is another option
DIMENSION = 8           # dimensions of a chess board are 8 x 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15            # for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
