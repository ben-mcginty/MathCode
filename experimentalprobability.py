import random
from tqdm import tqdm
from time import sleep
faverouble_outcome = 0

loopnumber = int(input("How many times would you like it to run? "))
print("")

for i in tqdm(range(loopnumber)):
    dice = random.randint(1,6)
    if dice >= 5:
        faverouble_outcome +=1

print("")
print("{:.1%}".format(faverouble_outcome/loopnumber))