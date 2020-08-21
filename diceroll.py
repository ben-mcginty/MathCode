import random
from tqdm import tqdm
from time import sleep

loopnumberSTR = input("How many runs would you like? ")
print("")
loopnumber = int(loopnumberSTR)
matchOverOrEqualTo3 = 0
matchLessThan3 = 0

for i in tqdm(range(loopnumber)):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    roll5 = random.randint(1,6)
    if roll1 == roll2 == roll3 or roll1 == roll2 == roll4 or roll1 == roll2 == roll5 or roll1 == roll3 == roll4 or roll1 == roll3 == roll5 or  roll1 == roll4 == roll5 or roll2 == roll3 == roll4 or roll2 == roll4 == roll5 or roll2 == roll4 == roll5 or roll3 == roll4 == roll5:
        matchOverOrEqualTo3 += 1
    else:
        matchLessThan3 += 1

print("")    
print("3 or more matches: ",matchOverOrEqualTo3)
print("Less than 3 matches: ",matchLessThan3)
print("3 or more matches: ","{:.1%}".format(matchOverOrEqualTo3/loopnumber))
print("Less than 3 matches: ","{:.1%}".format(matchLessThan3/loopnumber))