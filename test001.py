import os


columns1=[
["1","2","3"],
["4","5","6"],
["7","8","9"]
]

columns=[
[" "," "," "],
[" "," "," "],
[" "," "," "]
]
player=False
player_sign=("x","o")[player]
count=0
def show():
    global player_sign
    os.system("cls")
    for x in range(3):
        for y in range(3):
            print(" {}".format(columns1[x][y]),end=" ")
            if y is not len(columns1[x])-1:
                print("|",end='')
        if x is not len(columns1)-1:
           print('\n  -  -  -')
    print("\n__________________\n")
    for x in range(3):
        for y in range(3):
            print(" {}".format(columns[x][y]),end=" ")
            if y is not len(columns[x])-1:
                print("|",end='')
        if x is not len(columns)-1:
           print('\n  -  -  -')
    if count is not 9:
        chk_win(player_sign)
        player_sign=("x","o")[player]
        print("\nPlayer {} round\n".format(player_sign))
        insert_num=int(input("\n"));
        
        insert(insert_num,player_sign)
    else:
        exit("\n\n\n Game finished\n\n\n")
    

def insert(insert_num,player_sign):
    if 0<=insert_num<=9:
        global player
        global count
        if 1<=insert_num<=3:
            outter_index= ((insert_num+(3-insert_num))/3)-1
        elif 4<=insert_num<=6:
            outter_index= ((insert_num+(6-insert_num))/3)-1
        elif 7<=insert_num<=9:
            outter_index= ((insert_num+(9-insert_num))/3)-1
        outter_index=int(outter_index)
        inner_index=(insert_num-1%3)%3
        if columns[outter_index][inner_index] is " ":
            columns[outter_index][inner_index]=player_sign
            player= not(player)
            count+=1
    show()

def chk_win(player_sign):
    win_seq=set()
    for x in range(3):
        for y in range(3):
            if columns[x][y]==player_sign:
                if x==0:
                    win_seq.add(x+y+1)
                elif x==1:
                    win_seq.add(3+y+1)
                elif x==2:
                    win_seq.add(6+y+1)
    if {1,2,3}.issubset(win_seq) or {4,5,6}.issubset(win_seq) or {7,8,9}.issubset(win_seq) or {1,5,9}.issubset(win_seq) or {3,5,7}.issubset(win_seq) or {1,4,7}.issubset(win_seq) or {2,5,8}.issubset(win_seq) or {3,6,9}.issubset(win_seq):
        exit("\n\n\n{} is the winner\n\n\n".format(player_sign))
show()


    
