
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

def compAlgorithm():
	move = 1
	while (move):
		#check to try and get 3 in a row...
		move = 0

def validate(move):
	if board[move] == ' ' and move >= 0 and move <= 8:
		return True
	return False

def boardFull():
	for cell in board:
		if cell == ' ':
			return False
	return True

# def check2InARow():

def checkWin(index, xo):
	if index == 0:
		if board[3] == xo and board[6] == xo: #vertical
			return True
		if board[1] == xo and board[2] == xo: #horizontal
			return True
		if board[4] == xo and board[8] == xo: #diagonal
			return True
	if index == 1:
		if board[4] == xo and board[7] == xo: #vertical
			return True
		if board[0] == xo and board[2] == xo: #horizontal
			return True
	if index == 2:
		if board[5] == xo and board[8] == xo: #vertical
			return True
		if board[0] == xo and board[1] == xo: #horizontal
			return True
		if board[4] == xo and board[6] == xo: #diagonal
			return True
	if index == 3:
		if board[0] == xo and board[6] == xo: #vertical
			return True
		if board[4] == xo and board[5] == xo: #horizontal
			return True
	if index == 4:
		if board[1] == xo and board[7] == xo: #vertical
			return True
		if board[3] == xo and board[5] == xo: #horizontal
			return True
		if board[0] == xo and board[8] == xo: #diagonal1
			return True
		if board[2] == xo and board[6] == xo: #diagonal2
			return True
	if index == 5:
		if board[2] == xo and board[8] == xo: #vertical
			return True
		if board[4] == xo and board[3] == xo: #horizontal
			return True
	if index == 6:
		if board[4] == xo and board[0] == xo: #vertical
			return True
		if board[7] == xo and board[8] == xo: #horizontal
			return True
		if board[4] == xo and board[2] == xo: #diagonal
			return True
	if index == 7:
		if board[4] == xo and board[1] == xo: #vertical
			return True
		if board[6] == xo and board[8] == xo: #horizontal
			return True
	if index == 8:
		if board[5] == xo and board[2] == xo: #vertical
			return True
		if board[6] == xo and board[7] == xo: #horizontal
			return True
		if board[4] == xo and board[0] == xo: #diagonal
			return True
	return False

def game():
	mode = var[0]
	if var[1] == 'x':
		opponent1 = 'x'
		opponent2 = 'o'
	else:
		opponent1 = 'o'
		opponent2 = 'x'
	print(mode)
	if mode == '1': # ask player 1 for the moves and have computer respond with other char
		mode1()
	if mode == '2': # ask player 1 and then ask player 2 VALIDATE
		full = boardFull()
		while not full and var[3] == '-1':
			mode2(opponent1)
			if var[3] == '-1':
				mode2(opponent2)
		print(var[2])
	if mode == '3': # human watches comp play itself
		# COMPUTER MOVE X2
		compAlgorithm()
	print("Game is done!")
	print("Thank you for playing!")

def mode1():
	move1 = raw_input("Indicate the index you would like to place your " + opponent1 + " ")
	validate(int(move1))
	board[int(move1)] = opponent1
	# COMPUTER MOVE

def mode2(opponent):
	valid = 0
	while not valid:
		move = raw_input("Indicate the index you would like to place your " + opponent + " ")
		if validate(int(move)):
			board[int(move)] = opponent
			valid = 1
			if checkWin(int(move), opponent):
				if opponent == var[1]:
					var[2] = "Person1 won!"
					var[3] = 1
				else:
					var[2] = "Person2 won!"
					var[3] = 2
				printBoard()
				return
		else:
			print("Invalid input")
		printBoard()
		full = boardFull()
		if full:
			var[3] = 0
			break
# MAIN
board = [' ',' ',' ',
		' ',' ',' ',
		' ',' ',' '] # board in list form 0-8

# corners: 0, 2, 6, 8
# center: 4

#scores[0,0]
var = ['0','0','It is a tie!', '-1']
intro()
game()
# mode()
# user1()
