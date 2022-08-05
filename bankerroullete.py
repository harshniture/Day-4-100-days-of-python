import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

a = len(names)
b = random.randint(0, a-1)
c = names[b]
print(c + " is going to buy the meal today!")

