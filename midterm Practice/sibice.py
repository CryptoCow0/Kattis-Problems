import math
NumberOfMatches, Width, Height = input().split()
arr=[]
Hypotnuse = math.sqrt(int(Width)**2+int(Height)**2)
for x in range(int(NumberOfMatches)):
    temp = input()
    temp = int(temp)

    if (temp > int(Width) and temp > int(Height) and temp > Hypotnuse):
        arr.append("NE")
    else:
        arr.append("DA")

for x in arr:
    print(x)