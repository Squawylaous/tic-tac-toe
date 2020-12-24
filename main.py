def prep(x):
    if x==0: y=" "
    elif x==1: y="X"
    elif x==2: y="O"
    return y
def out(t3): print(" "+prep(t3[0]),"│",prep(t3[1]),"│",prep(t3[2]),"\n───┼───┼───\n",prep(t3[3]),"│",prep(t3[4]),"│",prep(t3[5]),"\n───┼───┼───\n",prep(t3[6]),"│",prep(t3[7]),"│",prep(t3[8]))
def check(t3):
    x=0
    for i in range(9):
        if t3[i]!=0: x+=1
    if x<5: y=0
    elif t3[4]==((t3[0] and t3[8])or(t3[2] and t3[6])or(t3[1] and t3[7])or(t3[3] and t3[5])) and t3[4]!=0: y=t3[4]
    elif t3[1]==(t3[0] and t3[2]) or t3[3]==(t3[6] and t3[0]) and t3[0]!=0: y=t3[0]
    elif t3[7]==(t3[6] and t3[8]) or t3[5]==(t3[2] and t3[8]) and t3[8]!=0: y=t3[8]
    elif x==9: y=3
    else: y=0
    return y
def turn(x,t3,p):
    t3[x-1]=p
    out(t3)
    return t3
# X │ X │ X
#───┼───┼───
# X │ X │ X
#───┼───┼───
# X │ X │ X
play="y"
while play=="Y" or play=="y":
    t3=[0,0,0,0,0,0,0,0,0]
    w=0
    p=2
    c=input("Do you want to play against another person? Y/N ")
    out(t3)
    while w==0:
        if p==2: p=1
        else: p=2
        if c=="Y" or c=="y" or p==1: x=int(input("Player "+str(p)+"'s turn. Input 1-9 to play. "))
        else: x=5
        l=0
        while t3[x-1]!=0:
            if c=="Y" or c=="y" or p==1: x=int(input("Player "+str(p)+"'s turn. Input 1-9 to play. "))
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
        t3=turn(x,t3,p)
        w=check(t3)
    if w==3: print("Tie!")
    else: print("Player",w,"wins! Congratulations!")
    play=input("Do you want to play again? (Y/N) ")
print("Goodbye!")
