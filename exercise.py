#Importing Libraries
import random
choice = {1:"O", 2:"X"}
#Input names of the players
print("Enter the names of the two players")
names=[]
names.append(input("Enter the name of player 1 : "))
names.append(input("Enter the name of player 2 : "))
#Randomly giving them "X" or "O"
a=random.randint(1,2)
b=0
if a==1:
    b=2
else:
    b=1
pl1="Player 1"
pl2="Player 2"
#Saving choices
sym = {pl1:choice[a], pl2:choice[b]}
print("Player 1 has "+sym[pl1])
print("Player 2 has "+sym[pl2])
#Initialize Board
a=[" "," "," "," "," "," "," "," "," "]
board=[[a[0]+"|"+a[1]+"|"+a[2]],[a[3]+"|"+a[4]+"|"+a[5]],[a[6]+"|"+a[7]+"|"+a[8]]]
#Printing the board
def print_board():
    board=[[a[0]+"|"+a[1]+"|"+a[2]],[a[3]+"|"+a[4]+"|"+a[5]],[a[6]+"|"+a[7]+"|"+a[8]]]
    for i in board:
        print(i)

#Check if any player has won the game or not

def check(s):
    if a[0]==a[1]==a[2]==s or a[0]==a[4]==a[8]==s or a[0]==a[3]==a[6]==s or a[3]==a[4]==a[5]==s or a[6]==a[7]==a[8]==s:
        return True
    elif a[1]==a[4]==a[7]==s or a[2]==a[5]==a[8]==s or a[2]==a[4]==a[6]==s:
        return True
    else:
        return False


print_board()
#Loop until someone wins the game or it becomes a tie
gaming = True
while gaming == True:
    valid=False
    #Checking validity of player1's input
    while valid!=True:
        pos1=int(input("Player 1, Enter your position : "))
        if pos1>9 or pos1<1 or (a[(pos1-1)]==sym[pl1]) or (a[(pos1-1)]==sym[pl2]):
            print("Wrong input")
            valid=False
        else:
            valid=True
    a[(pos1-1)]=sym[pl1]
    print_board()
    p1=check(sym[pl1])
    #check if player 1 has won or not
    if p1==True:
        print("Game over! "+names[0]+" has won the game")
        gaming=False
        break
    #check the if it is a tie
    gamer=True
    for i in a:
        if i==" ":
            gamer=False
            break
    if gamer==True:
        print("Oops! This is a Tie!")
        gaming=False
        break
    valid=False
    #Check the validity of player2's input
    while valid!=True:
        pos2=int(input("Player 2, Enter your position : "))
        if pos2>9 or pos2<1 or (a[(pos2-1)]==sym[pl2]) or (a[(pos2-1)]==sym[pl1]):
            print("Wrong input")
            valid=False
        else:
            valid=True
    a[(pos2-1)]=sym[pl2]
    print_board()
    p2=check(sym[pl2])
    

    #check if player2 has won the game or not
    if p2==True:
        print("Game over! "+names[1]+" has won the game")
        gaming=False
        break
    #check if it is a tie
    gamer=True
    for i in a:
        if i==" ":
            gamer=False
            break
    if gamer==True:
        print("Oops! This is a Tie!")
        gaming=False
