from enum import Enum

class PieceType(Enum): # This can be moved to seperated file as well.
    X = 'X'
    O = 'O'

class Piece:
    def __init__(self, pieceType):
        self.pieceType = pieceType
    def __str__(self):
        return self.pieceType.value

class PieceO(Piece):
    def __init__(self):
        super().__init__(PieceType.O)

class PieceX(Piece):
    def __init__(self):
        super().__init__(PieceType.X)
