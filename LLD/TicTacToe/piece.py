from enum import Enum

class PieceType(Enum):
    X = 'X'
    O = 'O'

class Piece:
  def __init__(self,pieceType):
    self.pieceType =  pieceType


class PieceO(Piece):
  def __init__():
    super.__init__(pieceType.O)

class PieceX(Piece):
  def __init__():
    super.__init__(pieceType.X)
