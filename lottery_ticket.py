

def lucky_number(n):
    n=str(n)
    n=[ int(letter) for letter in n ]
    return sum(n[:int(len(n)/2)])==sum(n[int(len(n)/2):])

lucky_number(1203)


def isLucky(n):
    n=list(map(int,list(str(n))))
    return sum(n[:int(len(n)/2)])==sum(n[int(len(n)/2):])

