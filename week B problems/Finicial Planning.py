'''
Programmer Name: Miguel Wills
Program Purpose: Determine when to Retire based on Kattis ruberic
Date Written: 9/3/2023
'''
from itertools import combinations
amount, Retierment = input().split()

amount = int(amount)

Retierment = int(Retierment)

inputGiven = []

for x in range(0, amount):
    current = input().split()
    inputGiven.append(current)


potentialAnswers = []

for count in range(1, len(inputGiven)+1):
    for combo in combinations(inputGiven, count):
        value = sum(combo)-5
        if value == 7:
            print(combo, "value equals", value)




'''
for x in range(len(inputGiven)):
    #print(x)
    #print(inputGiven[x])
    counter = 1
    while(True):
       # if profit per day - cost >= Retierment
       if ((int(inputGiven[x][0]) * counter - int(inputGiven[x][1])) >= Retierment):
            potentialAnswers.append(counter)
            #print(x)
            break
       elif((int)(inputGiven[x][0] * counter + int(inputGiven[x + counter]) - (int(inputGiven[x[1]]  + inputGiven[x + counter][1] ) > = Retierment):
                  potentialAnswers.append(counter)
        
                  break
        
       counter +=1       
        '''
# find the smallest number in counter array then print it out







min = potentialAnswers[0]
for x in potentialAnswers:
    if(x < min):
        min = x
print(x)



















