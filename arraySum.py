#this is to check if any 2 numbers in an array add up to a given sum from the user, as well as the array is also from the use.

array = []
numsInArray = int(input("How many numbers are in your array? "))
addToArrayLoopCount = 0
indexNumber = 0
searchNum = 1

for i in range(numsInArray):
    addToArrayLoopCount += 1
    print("Loop ",addToArrayLoopCount," of ",numsInArray)
    numToAdd = int(input("What is the number to be added to the array? "))
    array.append(numToAdd)

sum = int(input("What is the number that you are trying to find? "))

for i in int(len(array)):
    searchNum += 1
    attemptFind = array[searchNum] - sum
    try:
        array.index(attemptFind)
    except:
        numberFound = false
    else:
        print("There has been a match founds, the two numbers are ",searchNum," and ",attemptFind,"!")


print(array)