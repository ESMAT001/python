from os import system
from random import randint

columns = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
player = True
count = 0
y_space = "\n"*9
x_space = "\t"*4


def main():
    if player:
        print_game()
    if count != 9:
        player_sign = ("x", "o")[not player]
        chk_win(player_sign)
        player_sign = 'x' if player else 'o'
        if player:
            val = int(input(f"\n\n\n{x_space}{player_sign} round :"))
            insert(val, player_sign)
        else:
            computer(player_sign)
        main()
    else:
        exit(f"\n\n{x_space}Game finished\n\n")


def print_game():
    system("cls")
    print(y_space, x_space, end="")
    for x in range(3):
        for y in range(3):
            print(f" {columns[x][y]}", end="")
            if y != 2:
                print(" |", end="")
        if x != 2:
            print(f"\n{x_space}--  ---  --\n{x_space}", end="")


def computer(player_sign):
    val = randint(1, 9)
    if 1 <= val <= 3:
        outter_index = ((val + (3 - val)) / 3) - 1
    elif 4 <= val <= 6:
        outter_index = ((val + (6 - val)) / 3) - 1
    elif 7 <= val <= 9:
        outter_index = ((val + (9 - val)) / 3) - 1
    outter_index = int(outter_index)
    inner_index = (val - 1 % 3) % 3
    if columns[outter_index][inner_index] == " ":
        insert(val, player_sign)
    else:
        computer(player_sign)


def insert(val, player_sign):
    global player, count
    if 1 <= val <= 9:
        if 1 <= val <= 3:
            outter_index = ((val + (3 - val)) / 3) - 1
        elif 4 <= val <= 6:
            outter_index = ((val + (6 - val)) / 3) - 1
        elif 7 <= val <= 9:
            outter_index = ((val + (9 - val)) / 3) - 1
        outter_index = int(outter_index)
        inner_index = (val - 1 % 3) % 3
        if columns[outter_index][inner_index] == " ":
            columns[outter_index][inner_index] = player_sign
            count += 1
            player = not (player)


def chk_win(player_sign):
    win_seq = set()
    for x in range(3):
        for y in range(3):
            if columns[x][y] == player_sign:
                if x == 0:
                    win_seq.add(x + y + 1)
                elif x == 1:
                    win_seq.add(3 + y + 1)
                elif x == 2:
                    win_seq.add(6+y+1)
    if {1, 2, 3}.issubset(win_seq) or \
        {4, 5, 6}.issubset(win_seq) or\
        {7, 8, 9}.issubset(win_seq) or\
        {1, 5, 9}.issubset(win_seq) or\
        {3, 5, 7}.issubset(win_seq) or\
        {1, 4, 7}.issubset(win_seq) or\
        {2, 5, 8}.issubset(win_seq) or\
            {3, 6, 9}.issubset(win_seq):
        print_game()
        x_space = '   '*9
        exit(
            f"\n\n{x_space}{'-'*19}\n{x_space}| The winner is {player_sign} |\n{x_space}{'-'*19}")


main()
