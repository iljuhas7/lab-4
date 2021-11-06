import random

Sum = random.randint(1, 9)
rNum = random.randint(2, 5)

print(Sum, end="")
for fNext in range(rNum):
    rSwitch = random.randint(1, 3)
    rAdd = random.randint(1, 9)

    if rSwitch == 0:
        print(" + ", rAdd, end="", sep="")
        Sum += rAdd

    elif rSwitch == 1:
        print(" - ", rAdd, end="", sep="")
        Sum -= rAdd

    elif rSwitch == 2:
        print(" * ", rAdd, end="", sep="")
        Sum *= rAdd

    else:
        print(" : ", rAdd, end="", sep="")
        Sum /= rAdd

print(" = ", end="")
uSum = float(input())

if float(Sum) == uSum:
    print(" Right! ")
else:
    print(" Wrong answer! \n Right answer: ", Sum)

