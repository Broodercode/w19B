import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2
board = gameboard.GameBoard()
player = player.Player(3, 2)


while True:
    print('inner function')
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")

    if(selection == 'a'):
        check = board.checkMove(player.rowPosition, player.columnPosition-1)
        if(check):
            print('a pressed')
            player.moveLeft()           
    elif(selection == 's'):
        check = board.checkMove(player.rowPosition+1, player.columnPosition)
        if(check):
            print('s pressed')
            player.moveDown()
    elif(selection == 'w'):
        check = board.checkMove(player.rowPosition-1, player.columnPosition)
        if(check):
            print('w pressed')
            player.moveUp()
    elif(selection == 'd'):
        check = board.checkMove(player.rowPosition, player.columnPosition+1)
        if(check):
            print('d pressed')
            player.moveRight()
    win = board.checkWin(player.rowPosition, player.columnPosition)
    if (win):
        print('Congratulations, you beat the game!')
        break   
    # TODO
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
