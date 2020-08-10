# Snake Water Gun Game

import random

print("Starting Snake Water Gun, 10 Rounds Per Game, One with Max Score Wins")
print("At Any Point Press 9 To exit")
computerScore = 0   # Score Handler For Computer Player
humanScore = 0    # Score Handler For Human Player
bool = True
round = 10

while(bool == True):

    if(round == 1):
        bool = False

    print(f"Round Number: {round}")
    round = round - 1
    choiceList = ["Snake", "Water", "Gun"]
    computerchoice = random.choice(choiceList)
    # print(computerchoice)

    print("Press 1 For Snake\n"
          "Press 2 For Water\n"
          "Press 3 For Gun\n"
          "Press Any other number to exit before 10 rounds\n"
          "Your Choice:")

    userchoice = int(input())

    if(userchoice == 1):
        print(f"You Selected Snake and Computer Selected {computerchoice}")

        if(computerchoice == "Gun"):
            computerScore = computerScore + 1
            print(f"You Lost!, Your Score:{humanScore} Computer Score:{computerScore} ")
        elif(computerchoice == "Snake"):
            print(f"Tie!, Your Score:{humanScore} Computer Score:{computerScore} ")
        else:
            humanScore = humanScore + 1
            print(f"You Won!, Your Score:{humanScore} Computer Score:{computerScore}")

    elif(userchoice == 2):
        print(f"You Selected Water and Computer Selected {computerchoice}")

        if (computerchoice == "Gun"):
            humanScore = humanScore + 1
            print(f"You Won!, Your Score:{humanScore} Computer Score:{computerScore}")
        elif (computerchoice == "Snake"):
            computerScore = computerScore + 1
            print(f"You Lost!, Your Score:{humanScore} Computer Score:{computerScore} ")
        else:
            print(f"Tie!, Your Score:{humanScore} Computer Score:{computerScore} ")


    elif(userchoice == 3):
        print(f"You Selected Gun and Computer Selected {computerchoice}")

        if (computerchoice == "Gun"):
            print(f"Tie!, Your Score:{humanScore} Computer Score:{computerScore} ")
        elif (computerchoice == "Snake"):
            humanScore = humanScore + 1
            print(f"You Won!, Your Score:{humanScore} Computer Score:{computerScore}")
        else:
            computerScore = computerScore + 1
            print(f"You Lost!, Your Score:{humanScore} Computer Score:{computerScore} ")
    else:
        bool = False

print("Game Ends, Results are being displayed")

if(humanScore > computerScore):
    print("Hurray, YOU WON THE GAME!")
elif(humanScore == computerScore):
    print("Oh Snap, Tie !")
else:
    print("Oh No, YOU LOST THE GAME!")