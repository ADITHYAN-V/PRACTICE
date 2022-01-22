print('''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/
''')
print("WELCOME TO BLACKJACK")
import random
cards_val={"A":[1,11],"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"K":10,"Q":10,"J":10}
cards=[]
for i in cards_val:
    cards.append(i)
ch="y"
def drawrandom(n,sit):#situation refers if the fn is used at the beginning or at the second draw. Helps in determining the value of ace
    '''Draws the given number of random cards and return the items and their values'''
    rand_cards=random.choices(cards,k=n)
    val=0
    for i in rand_cards:
        if i=="A":
            val+=cards_val[i][sit]
        else:
            val+=cards_val[i]
    return (rand_cards,int(val))
#_main_
while ch=="y":
    print("\n"*3)
    usercards,userval=drawrandom(2,1)
    if userval==21:
        print("BLACKJACK!)")
        bj=True
    elif userval==22:
        userval=1+11
    print(f"Your cards are {usercards} and their combined value is {userval}")
    compcards,compval=drawrandom(2,1)
    bj=False
    if compval==21:
        bj=True
    elif compval==22:
        compval=1+11
    initialoutputval=0
    initialoutputcard=[]
    initialoutputcard.append(compcards[0])
    for i in initialoutputcard:
        if i=="A":
            initialoutputval+=cards_val[i][1]
        else:
            initialoutputval+=cards_val[i]
    print(f"The computer first card is {initialoutputcard} whose value is {initialoutputval}")
    if bj==False:
        draw=input(f"Do you wanna draw another card? Remember your current score is already {userval}\n(y/n): ").lower()
        while draw=='y':
            if userval<10:
                sit=1
            else:
                sit=0
            tempcard,tempval=drawrandom(1,sit)
            userval+=tempval
            print(f"The current card drawn is {tempcard} and the net value is {userval}")
            if userval>=21:
                break
            else:
                draw=input(f"Do you wanna draw another card? Remember your current score is already {userval}\n(y/n): ").lower()
    if userval>21:
        print("BUST YOU LOOSE")
        ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
        continue
    else:
        print(f"The computer's cards were {compcards} and their net value is {compval}")
        while compval<17:
            if compval<10:
                sit=1
            else:
                sit=0
            tempcard,tempval=drawrandom(1,sit)
            compval+=tempval
            print(f"The computer's new card is {tempcard} and computers current net value is {compval}")
            if compval>=21:
                break
        if [compval,userval]==[21,21]:
            print("DOUBLE BLACKJACK SO ITS A DRAW")
            ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
            continue
        elif compval>21:
            print("BUST!! COMP LOOSES :)")
            ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
            continue
        elif compval==userval:
            print("DRAW!!")
            ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
            continue
        elif compval>userval:
            print("COMPUTER WINS!!")
            ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
            continue
        elif userval>compval:
            print("YOU WIN")
            ch=input("Do you wanna play BLACKJACK again?(y/n)").lower()
            continue
        else:
            print("PROGRAMMER IS MAD")

print("\n"*2,"THANKYOU","\n"*2)
