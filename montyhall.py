import random
from tqdm import tqdm
from time import sleep

loopnumberSTR = input("How many times would you like each phase to run? ")
print("")
loopnumber = int(loopnumberSTR)

loopcount = 1
times_won_switch = 0
times_lost_switch = 0
times_won_stay = 0
times_lost_stay = 0
print("Stay phase in progress...")

#perfroming stay phase
for i in tqdm(range(loopnumber)):
    #defineing random doorsa
    prize_door = random.randint(1,3)
    chosen_door = random.randint(1,3)
    #comparing door data
    if prize_door == chosen_door:
        times_won_stay += 1
    elif  prize_door != chosen_door:
        times_lost_stay += 1

loopcount = 1
print("Stay phase complete. ✔")
print("")
print("Switch phase in progress...")
opened_door = 0


for i in tqdm(range(loopnumber)):
    #generating random doors
    prize_door = random.randint(1,3)
    chosen_door = random.randint(1,3)

    #'opening' door for switching doors
    if prize_door != 1 and chosen_door != 1:
        opened_door = 1
    elif prize_door != 2 and chosen_door != 2:
        opened_door = 2
    elif prize_door != 3 and chosen_door != 3:
        opened_door = 3

    #switching doors
    switched_door = 0
    if prize_door != chosen_door:
        switched_door = prize_door
    elif prize_door == chosen_door and prize_door != 1 and opened_door != 1:
        switched_door = 1
    elif prize_door == chosen_door and prize_door != 2 and opened_door != 2:
        switched_door = 2
    elif prize_door == chosen_door and prize_door != 3 and opened_door != 3:
        switched_door = 3

    if prize_door == switched_door:
        times_won_switch += 1
    elif prize_door != switched_door:
        times_lost_switch += 1


print("Switch phase complete. ✔")
print("")
print("Times lost stay, ",times_lost_stay)
print("Times won stay, ",times_won_stay)
print("Times lost switch, ",times_lost_switch)
print("Times won switch, ",times_won_switch)
print("Average of win when switching is ","{:.1%}".format(times_won_switch/loopnumber))
print("Average of loss when switching is ","{:.1%}".format(times_lost_switch/loopnumber))
print("Average of win when staying is ","{:.1%}".format(times_won_switch/loopnumber))
print("Average of loss when switching is ","{:.1%}".format(times_lost_switch/loopnumber))
print("")