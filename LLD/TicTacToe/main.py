from board import Board
from player import Player
from piece import PieceX, PieceO
from tictactoe import TicTacToe

if __name__ == "__main__":
    """
    This is the main file for the Tic Tac Toe game.
    It contains the main function that runs the game.
    """
    # Create board
    board = Board(size=3)
    # Create players with their pieces
    player1 = Player("Bob", PieceX())
    player2 = Player("Balli", PieceO())
    # Create game
    game = TicTacToe(board, [player1, player2])
    # Start the game
    game.startGame()