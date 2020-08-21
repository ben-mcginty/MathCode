from tqdm import tqdm
from time import sleep
loops = int(input("How many times would you like to loop it? "))
sum = 0
loopnumber = 0

for i in tqdm(range(loops)):
    if (loopnumber%3==0) or (loopnumber%5==0):
        sum = loopnumber + sum
    
    loopnumber += 1

print("The sum is ",sum)