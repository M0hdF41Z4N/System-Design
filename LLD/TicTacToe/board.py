class Board:
    def __init__(self, size=3):
        self.size = size
        # Use list comprehension to avoid shared row references
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def addPiece(self, row, col, piece):
        # Add the piece to the board
        if self.board[row][col] is None:
            self.board[row][col] = piece
            return True
        return False

    def getFreeCells(self):
        count = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    count += 1
        return count

    def printBoard(self):
        for row in range(self.size):
            print(' '.join(str(self.board[row][col]) if self.board[row][col] is not None else '-' for col in range(self.size)))
        print()
