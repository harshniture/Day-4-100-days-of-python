#Rock Paper Scissor Game

import random

print("Welcome to Rock Paper Scissor Game ! ")

a = int(input("What do you wamt to choose? 1 for Rock 2 for Paper 3 for Scissor: "))
b = random.randint(1,3)

if a == 1:
    print("You chose Rock")
    if b == 1:
        print("Computer chose Rock")
        print("It's a tie")
    elif b == 2:
        print("Computer chose Paper")
        print("You lose")
    else:
        print("Computer chose Scissor")
        print("You win")
elif a == 2:
    print("You chose Paper")
    if b == 1:
        print("Computer chose Rock")
        print("You win")
    elif b == 2:
        print("Computer chose Paper")
        print("It's a tie")
    else:
        print("Computer chose Scissor")
        print("You lose")
elif a == 3:
    print("You chose Scissor")
    if b == 1:
        print("Computer chose Rock")
        print("You lose")
    elif b == 2:
        print("Computer chose Paper")
        print("You win")
    else:
        print("Computer chose Scissor")
        print("It's a tie")
    