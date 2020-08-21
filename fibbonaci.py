a = 1
b = 2
s = 0
loopnumber = int(input("How many loops? "))
while b <= loopnumber:
    s += b
    a,b = a*1+b*2,a*2+b*3
print(s)