# #random number generator module

# c = random.randint(100,1000)
# print(c)

import random	 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)


c =  random.randint(0,1)
if c == 0:
    print("Tails")
else:
    print("Heads")