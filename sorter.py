array = []
loopNumber = int(input("How many numbers are to be sorted? "))
for i in range(loopNumber):
    num = int(input("What is the number to be added? "))
    array.append(num)
sortedList = sorted(array)
print("The sorted list is: ",sortedList)
print("The original list is ", array)