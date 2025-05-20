class Board:
  def __init__(self,size=3):
    self.size = size
    self.board = [ [None] * size ] * size

  def addPiece(row,col,piece):
    self.board[row][col] = piece

  def getFreeCells():
    count = 0
    for row in self.size:
      for col in self.size:
        if not self.board[row][col]:
          count += 1
    return count


  def printBoard():
    for row in self.size:
      for col in self.size:
        print(self.board[row][col],sep=" ")
      print("/n")
