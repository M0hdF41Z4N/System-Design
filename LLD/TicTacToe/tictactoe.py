from collections import deque
from piece import PieceX, PieceO
from player import Player
from board import Board

class TicTacToe:
  def __init__(self, board=None, players=None):
    self.board = board
    self.players = deque(players) if players else deque()
    self.winner = None

  def initializeGame(self):
    # Initialize Piece or get players and their pieces in arguments
    
    crossPiece = PieceX()
    KnotPiece = PieceO()
    
    # Assign Piece to players
    PlayerOne , PlayerTwo = Player("Bob",crossPiece), Player("Balli",KnotPiece)

    self.players.append(PlayerOne)
    self.players.append(PlayerTwo)
    self.size = 3
    self.board = Board(self.size)
    self.board.printBoard()
    print("Game Initialized! Players are ready to play!")

    

  def startGame(self):
    # Initialize the game
    self.initializeGame();
    
    noWinner = True
    while noWinner:
      # Get player which has turn
      playerWithTurn = self.players.popleft()

      # Check if board has empty cells
      if not self.board.getFreeCells():
        noWinner = False
        continue

      # Print the board
      self.board.printBoard()

      print(f"{playerWithTurn.name} has turn! please select the position seperated with space.");

      # Get row and cols from player
      try:
          row, col = map(int, input().split())
      except Exception:
          print("Invalid input! Please enter two numbers.")
          self.players.appendleft(playerWithTurn)
          continue
      if row < 0 or row >= self.size or col < 0 or col >= self.size or self.board.board[row][col] is not None:
          print("Invalid move! Try again.")
          self.players.appendleft(playerWithTurn)
          continue
      
      # Check if position is empty
      if (self.board.board[row][col]):
        self.players.appendleft(playerWithTurn)
        print("Invalid Input! Try Again")
        continue


      # Mark the board with piece
      self.board.addPiece(row,col,playerWithTurn.piece)

      
      # Check Winner
      winner = self.checkWinner(row,col,playerWithTurn.piece)
      if winner:
        self.winner = playerWithTurn;
        return self.winner.name
      
      # toggle the player
      self.players.append(playerWithTurn)
    return "No Winner! Game is Draw!"

      
      

      

      
      

  def checkWinner(self, curr_row, curr_col, piece):
    
    # Check horizontal
    horizontal = all(str(self.board.board[curr_row][col]) == str(piece) for col in range(self.size))
    if horizontal:
      return True

    # Check vertical
    vertical = all(str(self.board.board[row][curr_col]) == str(piece) for row in range(self.size))
    if vertical:
      return True

    # Check left diagonal (top-left to bottom-right)
    if curr_row == curr_col:
      left_diag = all(str(self.board.board[i][i]) == str(piece) for i in range(self.size))
      if left_diag:
        return True

    # Check right diagonal (top-right to bottom-left)
    if curr_row + curr_col == self.size - 1:
      right_diag = all(str(self.board.board[i][self.size - 1 - i]) == str(piece) for i in range(self.size))
      if right_diag:
        return True

    return False 
