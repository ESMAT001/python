import os
from time import sleep
space = " "
num = 0


def refresh():
    global num
    os.system("cls")
    print(f"|--~{space*num}-")
    s
    num += 1
    refresh()


refresh()
