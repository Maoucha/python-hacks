from random import randint

board = []

# Set up the battlefield by creating a board containing 5 lists of 5 eletments each
for x in range(0, 5):
    board.append(["O"] * 5)

# Set the lists as a grid
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

# Use randint function to return a random position for a row and a column
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Define variables for the ship position (row, col) and the position the player will guess (row, col)
for turn in range(4):
	ship_row = random_row(board)
	ship_col = random_col(board)
	guess_row = int(raw_input("Guess Row:"))
	guess_col = int(raw_input("Guess Col:"))

# Display messages after the player took a guess
	if guess_row == ship_row and guess_col == ship_col:
    	print "Congratulations! You sank my battleship!"
    	break
	else:
		if guess_row not in range(5) or guess_col not in range(5):
    		print "Oops, that's not even in the ocean."
		elif  board[guess_row][guess_col] == "X":
    		print "You guessed that one already."    
		else:
    		print "You missed my battleship!"
    		board[guess_row][guess_col] = "X"
    	print "Turn", turn + 1
    if turn == 3:
        print "Game Over"
    print_board(board)