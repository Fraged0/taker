import colorama
import random

colorama.init()
colorama.just_fix_windows_console()

colors = {0: colorama.Back.WHITE, 1: colorama.Back.RED}
board = [0 ,0, 0, 0, 0, 0, 0, 0, 0, 0]

def render():
    global board
    render = ""
    for clr in board:
        render += colors[clr] + "  "
    return render

while True:
    print(render() + colorama.Back.RESET)
    inp = int(input("> ")) - 1
    board[inp] = 1
    for i in range(2):
        toDel = random.randrange(0, 10)
        while toDel == inp:
            toDel = random.randrange(0, 10)
        board[toDel] = 0
