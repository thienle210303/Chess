"""
Main driver file
    Responsible for handling user input
    displaying the current GameState Object
"""

import pygame as p

import ChessEngine

WIDTH = HEIGHT = 512    # 400 is another option
DIMENSION = 8           # dimensions of a chess board are 8 x 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15            # for animations later on
IMAGES = {}


def loadImages():
    """ Initialize a global dictionary of images. This will be called exactly once in the main """
    types = ["R", "N", "B", "Q", "K", "B", "N", "R", "P"]
    color = ['w', 'b']
    pieces = [f"{c}{t}" for c in color for t in types]
    for piece in pieces:
        # load image and scale image
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying 'IMAGES['wp']'


def main():
    """
    The main driver responsible for handling input and game state
    """
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    loadImages()    # only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    """ Responsible for all the graphics within a current game state """
    drawBoard(screen, gs.board)               # draw squares on the board
    # add in piece highlighting or move suggestions (later)


def drawBoard(screen, board):
    """ Draw the squares and the pieces on the board """
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            # draw color board
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

            # draw pieces
            piece = board[r][c]
            if piece != "--":  # not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()