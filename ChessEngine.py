"""
Class is responsible for:
    1) storing all the information about the current state of a chess game.
    2) determining the valid moves at the current state.
    3) Keep a move log
"""


class GameState():
    def __init__(self):
        # board is 8x8 (2d list), each elem has 2 char
        # First char represents the color of piece: 'b' or 'w'
        # Second char represents the type of piece: 'K', 'Q', 'R', 'B', 'N' or 'P'

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []
