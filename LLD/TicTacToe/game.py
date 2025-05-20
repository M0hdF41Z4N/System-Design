import deque from deque

class Game:
  def __init__(self,board,players):
    self.board = board
    self.players = deque(players)
    self.winner = None

  def initializeGame():
    # Initialize Piece or get players and their pieces in arguments
    
    PieceX = new PieceX('X');
    PieceO = new PieceX('O');
    
    # Assign Piece to players
    PlayerOne , PlayerTwo = self.players
    
    PlayerOne.setPlayingPiece(PieceX)
    PlayerTwo.setPlayingPiece(PieceO)

    

  def startGame():
    # Initialize the game
    self.initializeGame();
    
    isWinner = None
    while not isWinner:
      # Get player which has turn
      playerWithTurn = self.players.popleft()

      print(f"{playerWithTurn.name} has turn! please select the position seperated with space.");

      # Get row and cols from player
      number(row) , number(col) = input().split(" ")
      
      # Check if position is empty
      if (self.board[row][col]):
        self.players.appendleft(playerWithTurn)
        print("Invalid Input! Try Again")
        continue


      # Mark the board with piece
      self.board[row][col] = playerWithTurn.piece

      
      # Check Winner
      isWinner = self.checkWinner(row,col,playerWithTurn.piece)
      if isWinner:
        self.winner = playerWithTurn;
        print(f"{winner.name} is the Winner !!!");

      
      # Check if board has empty cells
      if not self.board.getFreeCells():
        print("It's a Tie")

      # toggle the player
      self.players.append(playerWithTurn)

      
      

  def checkWinner(curr_row,curr_col,piece):
    # check horizontal
    horizontal = True
    for col in range(self.size):
      if self.board[curr_row][col] != piece:
        horizontal = False
        break

    if horizontal:
      return horizontal
      
    # check vertical
    vertical = True
    for row in range(self.size):
          if self.board[row][curr_col] != piece:
            vertical = False
            break
    
    if vertical:
      return vertical


    leftDiag = True
    # check left diagonal
    row , col = curr_row , curr_col
    while row < self.size and col < self.size:
      if not self.board[row][col] != piece:
            leftDiag = False
            break
      row+=1
      col+=1
    row , col =  curr_row , curr_col
    while row >= 0 and col >= 0:
      if not self.board[row][col] != piece:
            leftDiag = False
            break
      row-=1
      col-=1
    if leftDiag:
      return leftDiag
    # check right diagonal
    rightDiag = True
    row , col = curr_row , curr_col
    while row >= 0 and col < self.size:
      if not self.board[row][col] != piece:
            rightDiag = False
            break
      row-=1
      col+=1
    row , col =  curr_row , curr_col
    while row < self.size and col >= 0:
      if not self.board[row][col] != piece:
            rightDiag = False
            break
      row+=1
      col-=1
    if rightDiag:
      return rightDiag
    return False
    
