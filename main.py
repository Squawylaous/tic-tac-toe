def prep(x):
    if x==0: y=" "
    elif x==1: y="X"
    elif x==2: y="O"
    return y
def out(t3): print("",prep(t3[0][0]),"│",prep(t3[0][1]),"│",prep(t3[0][2])," │ ",prep(t3[1][0]),"│",prep(t3[1][1]),"│",prep(t3[1][2])," │ ",prep(t3[2][0]),"│",prep(t3[2][1]),"│",prep(t3[2][2]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[0][3]),"│",prep(t3[0][4]),"│",prep(t3[0][5])," │ ",prep(t3[1][3]),"│",prep(t3[1][4]),"│",prep(t3[1][5])," │ ",prep(t3[2][3]),"│",prep(t3[2][4]),"│",prep(t3[2][5]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[0][6]),"│",prep(t3[0][7]),"│",prep(t3[0][8])," │ ",prep(t3[1][6]),"│",prep(t3[1][7]),"│",prep(t3[1][8])," │ ",prep(t3[2][6]),"│",prep(t3[2][7]),"│",prep(t3[2][8]),"\n────────────┼─────────────┼────────────\n",prep(t3[3][0]),"│",prep(t3[3][1]),"│",prep(t3[3][2])," │ ",prep(t3[4][0]),"│",prep(t3[4][1]),"│",prep(t3[4][2])," │ ",prep(t3[5][0]),"│",prep(t3[5][1]),"│",prep(t3[5][2]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[3][3]),"│",prep(t3[3][4]),"│",prep(t3[3][5])," │ ",prep(t3[4][3]),"│",prep(t3[4][4]),"│",prep(t3[4][5])," │ ",prep(t3[5][3]),"│",prep(t3[5][4]),"│",prep(t3[5][5]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[3][6]),"│",prep(t3[3][7]),"│",prep(t3[3][8])," │ ",prep(t3[4][6]),"│",prep(t3[4][7]),"│",prep(t3[4][8])," │ ",prep(t3[5][6]),"│",prep(t3[5][7]),"│",prep(t3[5][8]),"\n────────────┼─────────────┼────────────\n",prep(t3[6][0]),"│",prep(t3[6][1]),"│",prep(t3[6][2])," │ ",prep(t3[7][0]),"│",prep(t3[7][1]),"│",prep(t3[7][2])," │ ",prep(t3[8][0]),"│",prep(t3[8][1]),"│",prep(t3[8][2]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[6][3]),"│",prep(t3[6][4]),"│",prep(t3[6][5])," │ ",prep(t3[7][3]),"│",prep(t3[7][4]),"│",prep(t3[7][5])," │ ",prep(t3[8][3]),"│",prep(t3[8][4]),"│",prep(t3[8][5]),"\n───┼───┼─── │ ───┼───┼─── │ ───┼───┼───\n",prep(t3[6][6]),"│",prep(t3[6][7]),"│",prep(t3[6][8])," │ ",prep(t3[7][6]),"│",prep(t3[7][7]),"│",prep(t3[7][8])," │ ",prep(t3[8][6]),"│",prep(t3[8][7]),"│",prep(t3[8][8])+"\n")
def check(t3):
    x=0
    for i in range(9):
        if t3[i]!=0: x+=1
    if x<3: y=0
    elif ((t3[4]==t3[0] and t3[4]==t3[8]) or (t3[4]==t3[2] and t3[4]==t3[6]) or (t3[4]==t3[1] and t3[4]==t3[7]) or (t3[4]==t3[3] and t3[4]==t3[5])) and t3[4]!=0: y=t3[4]
    elif (t3[1]==t3[0] and t3[1]==t3[2]) or (t3[3]==t3[6] and t3[3]==t3[0]) and t3[0]!=0: y=t3[0]
    elif (t3[7]==t3[6] and t3[7]==t3[8]) or (t3[5]==t3[2] and t3[5]==t3[8]) and t3[8]!=0: y=t3[8]
    elif x==9: y=3
    else: y=0
    return y
def turn(x,t3,p,y):
    t3[y-1][x-1]=p
    out(t3)
    return t3
# X │ X │ X
#───┼───┼───
# X │ X │ X
#───┼───┼───
# X │ X │ X
#
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#────────────┼─────────────┼────────────
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#────────────┼─────────────┼────────────
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
#───┼───┼─── │ ───┼───┼─── │ ───┼───┼───
# X │ X │ X  │  X │ X │ X  │  X │ X │ X 
play="y"
while play=="Y" or play=="y":
    t3=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    w=0
    p=2
    c=input("Do you want to play against another person? Y/N ")
    out(t3)
    y=5
    while w==0:
        if p==2: p=1
        else: p=2
        if y==10:
            if c=="Y" or c=="y" or p==1: y=int(input("Player "+str(p)+"'s turn. Input 1-9 to choose a board to play in. "))
            else: y=5
            l=0
            while t3[9][y-1]!=0:
                if c=="Y" or c=="y" or p==1: y=int(input("That board is completed. Input 1-9 to choose a board to play in. "))
                else:
                    if l==0: y=1
                    elif l==1: y=9
                    elif l==2: y=3
                    elif l==3: y=5
                    elif l==4: y=2
                    elif l==5: y=8
                    elif l==6: y=4
                    elif l==7: y=6
                    l+=1
            d=""
        else: d="Player "+str(p)+"'s turn. "
        if c=="Y" or c=="y" or p==1: x=int(input(d+"Input 1-9 to play. "))
        else: x=5
        l=0
        while t3[y-1][x-1]!=0:
            if c=="Y" or c=="y" or p==1: x=int(input("That space is taken. Input 1-9 to play. "))
            else:
                if l==0: x=1
                elif l==1: x=9
                elif l==2: x=3
                elif l==3: x=5
                elif l==4: x=2
                elif l==5: x=8
                elif l==6: x=4
                elif l==7: x=6
            l+=1
        t3=turn(x,t3,p,y)
        if t3[9][x-1]==0: y=x
        else: y=10
        for i in range(9): t3[9][i]=check(t3[i])
        w=check(t3[9])
    if w==3: print("Tie!")
    else: print("Player",w,"wins! Congratulations!")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
