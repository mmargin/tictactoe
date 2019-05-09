
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
	player1 = var[1]
	if mode == 1: # ask player 1 for the moves and have computer respond with other char
	if mode == 2: # ask player 1 and then ask player 2 VALIDATE
	if mode == 3: # human watches comp play itself


# MAIN
board = ['','','','','','','','',''] # board in list form 0-8

var = ['0','0']
intro()
mode()
user1()