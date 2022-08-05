#Rock Paper Scissor Game

import random

print("Welcome to Rock Paper Scissor Game ! ")

a = int(input("What do you wamt to choose? 1 for Rock 2 for Paper 3 for Scissor: "))
b = random.randint(1,3)

c = ["Rock", "Paper", "Scissor"]

print("you choose: " + c[a-1])
print("computer choose: " + c[b-1])

if a == b:
    print("It's a tie!")
elif a > b:
    print("You win!")
elif a == 1 and b == 3:
    print("You win!")
elif a < b:
    print("You lose!")
else:
    print("Invalid input , You lose !")