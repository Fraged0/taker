# required module
import random

# variables
colors = {0: '\033[0;37;47m', 1: '\033[0;37;41m', 2: '\033[0m'}
board = [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0]

# render the board
def render():
    global board
    render = ""
    for clr in board:
        render += colors[clr] + "  "
    return render

# run the game
while True:
    print(render() + colors[2])
    inp = int(input("> ")) - 1
    board[inp] = 1
    for i in range(2):
        toDel = random.randrange(0, 10)
        while toDel == inp:
            toDel = random.randrange(0, 10)
        board[toDel] = 0
