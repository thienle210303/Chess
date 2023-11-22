"""
Class is responsible for:
    1) storing all the information about the current state of a chess game.
    2) determining the valid moves at the current state.
    3) Keep a move log
"""


class GameState:
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
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        """ Take a Move  as a param and executes it (this will not work for castling, pawn promotion, and en-passant """
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove  # swap player

    def undoMove(self):
        """ Undo the last move """
        if len(self.moveLog) != 0:  # make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove  # switch turns back

    def getValidMoves(self):
        """ All move considering checks"""
        return self.getAllPossibleMoves()  # for now we will not worry about checks

    def getAllPossibleMoves(self):
        """ All move without considering checks"""
        moves = []
        for r in range(len(self.board))  # number of rows base on board
            for c in range(len(self.board[r])):  # number of cols in given row
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'P':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        return moves

    def getPawnMoves(self, r, c, moves):
        """ Get all the pawn moves for the pawn located at row, col and add these move to the list """


    def getRookMoves(self, r, c, moves):
        """ Get all the rook moves for the pawn located at row, col and add these move to the list """






class Move:
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRank = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSQ, endSQ, board):
        self.startRow = startSQ[0]
        self.startCol = startSQ[1]
        self.endRow = endSQ[0]
        self.endCol = endSQ[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    def __eq__(self, other):
        """ Override the equal method """
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        # You can add to make this like real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRank[r]