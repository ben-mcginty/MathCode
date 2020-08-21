import random
from tqdm import tqdm
from time import sleep

loopnumberSTR = input("How rolls would you like? ")
print("")
loopnumber = int(loopnumberSTR)
rollUnder10 = 0
rollOver10 = 0

for i in tqdm(range(loopnumber)):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = roll1+roll2
    if sum < 10:
        rollUnder10 += 1
    elif sum >= 10:
        rollOver10 += 1

print("")
print("--------------------------")
print("Rolls under 10: ",rollUnder10)
print("Rolls equal to or over 10: ",rollOver10)
print("Percentage under 10: ","{:.1%}".format(rollUnder10/loopnumber))
print("Percentage over or equal to 10: ","{:.1%}".format(rollOver10/loopnumber))
print("--------------------------")
print("")
print("")