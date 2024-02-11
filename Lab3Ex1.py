# lab3_NumTicTacToe.py

class NumTicTacToe:
    def __init__(self):
        # Initialize an empty 3 by 3 board
        self.size = 3
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def drawBoard(self):
        # Display the current state of the board with row and column indices
        print("  0 1 2")
        for i in range(self.size):
            print(f"{i} {'|'.join(map(str, self.board[i]))}")
            if i < self.size - 1:
                print(" " + "-" * (self.size * 2 - 1))

    def squareIsEmpty(self, row, col):
        # Check if the square at the given row and column indices is empty
        return self.board[row][col] == 0

    def update(self, row, col, num):
        # Update the square at the given row and column indices with the provided number
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else:
            return False

    def boardFull(self):
        # Check if the board is full (no empty squares)
        for row in self.board:
            if 0 in row:
                return False
        return True

    def isWinner(self):
        # Check if there is a line of three squares that adds up to 15
        # Check rows and columns
        for i in range(self.size):
            if sum(self.board[i]) == 15 or sum(self.board[row][i] for row in range(self.size)) == 15:
                return True

        # Check diagonals
        if sum(self.board[i][i] for i in range(self.size)) == 15 or sum(self.board[i][self.size - 1 - i] for i in range(self.size)) == 15:
            return True

        return False


# Integrated game flow

def play_game():
    print("---------------------------------------")
    print("Starting new Numerical Tic Tac Toe game")
    print("---------------------------------------")

    # Create an instance of NumTicTacToe
    game = NumTicTacToe()

    player_turn = 1

    while True:
        game.drawBoard()

        # Get input from the current player
        player_num = int(input(f"Player {player_turn}, please enter an {'odd' if player_turn == 1 else 'even'} number (1-9): "))
        row = int(input(f"Player {player_turn}, please enter a row: "))
        col = int(input(f"Player {player_turn}, please enter a column: "))

        # Update the board
        if player_turn == 1:
            while player_num % 2 == 0 or not game.update(row, col, player_num):
                print("Invalid input. Please enter a valid odd number.")
                player_num = int(input("Player 1, please enter an odd number (1-9): "))
        else:
            while player_num % 2 != 0 or not game.update(row, col, player_num):
                print("Invalid input. Please enter a valid even number.")
                player_num = int(input("Player 2, please enter an even number (2-8): "))

        # Check for a winner or a tie
        if game.isWinner():
            game.drawBoard()
            print(f"Player {player_turn} wins. Congrats!")
            break
        elif game.boardFull():
            game.drawBoard()
            print("It's a tie!")
            break

        # Switch to the next player's turn
        player_turn = 3 - player_turn  # Switch between player 1 and player 2

    play_again = input("Do you want to play another game? (Y/N) ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye.")
    else:
        play_game()

# Start the game
play_game()
