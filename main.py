"""
Making a Rock Paper and Scissors

"""
import random


print('Instructions are given below ')
print('Type 1,2,3 or R,P,S')
print("1: R for Rock")
print("2: P for Paper")
print("3: S for Scissors")
print('-------------------------------')

computerInput = random.randint(1, 3)
userInputs = input('Enter an number or character as instruct in above line:  ')
try:
    userInput = int(userInputs)

except:
    print(" ")
def game():

    if int(userInput)==computerInput:
        print("Draw")



    elif userInput == 1 and computerInput == 3:
        print('User Input : Rock   & Computer Input: Scissors')
        print()
        print('Users won')

    elif userInput == 2 and computerInput == 1:
        print('User Input : Paper   & Computer Input: Rock')
        print('UserWon')

    elif userInput ==3 and computerInput == 2:
        print('User Input : Scissors   & Computer Input: paper')
        print()
        print('User Won ')

    else:
     print('Computer Wins')

try:
    if (int(userInput) > 3):
        print("Read the instructions carefully")
    else:
       game()
except:
    print('Read the instructions carefully')
