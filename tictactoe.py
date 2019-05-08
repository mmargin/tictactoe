
def intro(mode, xo):
	print("Tic Tac Toe Game")
	print("This game can be played in 3 ways:")
	print("1) Person vs. Computer")
	print("2) Person vs. Person")
	print("3) Computer vs. Computer")

	start = 1
	while start == 1:
		mode = raw_input("Select a mode by indicating one number 1-3 ")
		if mode == '1':
			xo = raw_input("Would you, the Person, like to be 'x' or 'o'? " )
			if xo == 'x':
				print("That means that the Computer will be 'o'")
				start = 0
			elif xo == 'o':
				print("That means that the Computer will be 'x'")
				start = 0
			else:
				print("Invalid input")
		elif mode == '2':
			xo = raw_input("Would you, Person1, like to be x or o? ")
			if xo == 'x':
				print("That means that Person2 will be 'o'")
				start = 0
			elif xo == 'o':
				print("That means that Person2 will be 'x'")
				start = 0
			else:
				print("Invalid input")
		elif mode == '3':
			print("Computer1 will be 'x' and Computer2 will be 'o' ")
			start = 0
		else:
			print("Invalid input")
	
	raw_input("Press ENTER to continue ")

def game(mode):
	print(mode)
def user1(xo):
	print(xo)

player1 = ['','','','','','','','',''] # board in list form 0-8
player2 = ['','','','','','','','',''] # board in list form 0-8

mode = '0'
xo = 'x'
intro(mode, xo)
game(mode)
user1(xo)




