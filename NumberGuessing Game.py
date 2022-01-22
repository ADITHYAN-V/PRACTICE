print('''
   ___ _   _ ___ ___ ___   _____ _  _ ___   _  _ _   _ __  __ ___ ___ ___ 
  / __| | | | __/ __/ __| |_   _| || | __| | \| | | | |  \/  | _ | __| _ \
 | (_ | |_| | _|\__ \__ \   | | | __ | _|  | .` | |_| | |\/| | _ | _||   /
  \___|\___/|___|___|___/   |_| |_||_|___| |_|\_|\___/|_|  |_|___|___|_|_\
''')
import random
print('Welcome to the number guessing game')
ch="y"
while ch=='y':
    rang=int(input("The number to be guessed must be in between 0 and "))
    num=random.randint(0,rang)
    diff=input("Enter the difficulty level (Easy/Hard) :").lower()
    if diff=="hard":
        life=5
    else:
        life=10
    print(f"Total number of lifes = {life}")
    while life>0:
        print(f"{life} life/lives remain")
        guess=int(input("Enter your guess :"))
        if guess==num:
            print(f"Congrats you won with {life} life/lives remaining")
            break
        elif guess>num:
            print("High,Guess lower")
            life-=1
        elif guess<num:
            print("Low,Guess higher")
            life-=1
        else:
            print("PROGRAMMER IS MAD ERRORORORORROORORROROO")
            break
    if life==0:
        print(f"Sorry you lost the game.The number was {num}")
        ch=input("Wanna play again?(y/n) :").lower()
    elif guess==num:
        ch=input("Wanna play again?(y/n) :").lower()
print("\n"*2,"THANKU")
        
        
    
        





    
    
