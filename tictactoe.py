
def intro():
	print("***** Tic Tac Toe Game *****")
	print("This game can be played in 3 ways:")
	print("1) Person vs. Computer")
	print("2) Person vs. Person")
	print("3) Computer vs. Computer")

	start = 1
	while start == 1:
		var[0] = raw_input("Select a mode by indicating one number 1-3 ")
		if var[0] == '1':
			var[1] = raw_input("Would you, the Person, like to be 'x' or 'o'? " )
			xo = var[1]
			if xo == 'x':
				print("That means that the Computer will be 'o'")
				start = 0
			elif xo == 'o':
				print("That means that the Computer will be 'x'")
				start = 0
			else:
				print("Invalid input")
		elif var[0] == '2':
			var[1] = raw_input("Would you, Person1, like to be x or o? ")
			xo = var[1]
			if xo == 'x':
				print("That means that Person2 will be 'o'")
				start = 0
			elif xo == 'o':
				print("That means that Person2 will be 'x'")
				start = 0
			else:
				print("Invalid input")
		elif var[0] == '3':
			print("Computer1 will be 'x' and Computer2 will be 'o' ")
			start = 0
		else:
			print("Invalid input")	
	raw_input("Press ENTER to continue ")

def mode():
	return var[0] # MODE = var[0]

def user1():
	return var[1] # Player1 choice = var[1]

def printBoard():
	print(board[0] + '|' + board[1] + '|' + board[2])
	print('-----')
	print(board[3] + '|' + board[4] + '|' + board[5])
	print('-----')
	print(board[6] + '|' + board[7] + '|' + board[8])

def game():
	mode = var[0]
	if var[1] == 'x':
		opponent1 = 'x'
		opponent2 = 'o'
	else:
		opponent1 = 'o'
		opponent2 = 'x'
	print(mode)
	if mode == 1: # ask player 1 for the moves and have computer respond with other char
		move1 = raw_input("Indicate the index you would like to place your " + opponent1)
		validate(move1)
		board[move1] = opponent1
		# COMPUTER MOVE
	if mode == 2: # ask player 1 and then ask player 2 VALIDATE
		valid = 1
		while valid == 1:
			move1 = raw_input("Indicate the index you would like to place your " + opponent1)
			if validate(move1):
				board[move1] = opponent1
				valid = 0
			else:
				print("Invalid input")
		valid = 1
		while valid == 1:
			move2 = raw_input("Indicate the index you would like to place your " + opponent2)
			if validate(move2):
				board[move2] = opponent2
				valid = 0
			else:
				print("Invalid input")
	if mode == 3: # human watches comp play itself
		# COMPUTER MOVE X2
		compAlgorithm()

def compAlgorithm():
	move = 1
	while (move):
		#check to try and get 3 in a row...
		move = 0

def validate(move):
	if move >= 0 and move <= 8:
		if board[move] == '':
			return True
	return False

# MAIN
board = ['','','','','','','','',''] # board in list form 0-8

var = ['0','0']
intro()
game()
mode()
user1()
