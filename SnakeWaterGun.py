import random
import os

os.system('cls')
choiceList = ["s", "w", "g"]

def randomsel():
    compchoice = random.choice(choiceList)
    return compchoice
countComp = 0
countPlayer = 0

def winner(userchoice, compchoice):
    global countComp
    global countPlayer
    if userchoice == compchoice:
        winner1 = "Tie"

    elif userchoice == "s" and compchoice == "g" or userchoice == "w" and compchoice == "s" or userchoice == "g" and compchoice == "w":
        winner1 = "Bot"
        countComp += 1
    else:
        winner1 = "You" 
        countPlayer += 1
    return winner1

def error1():
    os.system('cls')
    print("ERROR!!! Please enter a valid input")
    inpmain()

def inpmain():
    print("How many rounds do you want to play?")
    rounds2 = input()
    os.system('cls')
    try:
        rounds2 = int(rounds2)
    except Exception as error:
        error1()
    return rounds2
def checker(userchoice):
    global rounds
    if userchoice != "s" and userchoice != "w" and userchoice != "g":
        print("PLease enter a valid input")
        play(rounds1)
    else:
        print()  

def play(rounds):
    i = 1
    while (i<=rounds):

        print(f"\t \t \t \t \t ***Snake Water Gun***")
        print()
        print(f"\t \t \t \t \t \t Round: {i}/{rounds}")
            
        print("Enter your choice" )
        userchoice = input()
        userchoice = userchoice.lower()
        checker(userchoice)

        compchoice = randomsel()
        print(f"Computer:{compchoice}")
        winner2 = winner(userchoice,compchoice)

        if winner2 == "Tie":
            print(f"{winner2}")
        else:    
            print(f"{winner2} Won")
        continue1 = input("Enter something to continue... ")
        os.system('cls')
        i += 1
rounds1 = inpmain()
play(rounds1)

print("Match Over")
print()
print(f"You: {countPlayer}")
print(f"Computer: {countComp}")
if countComp == countPlayer:
    print("Tie")
elif countComp > countPlayer:
    print("You Lost!")
else:
    print("You Won!!!")

print()
print("Do You want to play again?(Y/N)")
playa = input()

playa = playa.lower()
if playa == "y":
    rounds1 = inpmain()
    play(rounds1)
else:
    print("Thank You For Playing! ")