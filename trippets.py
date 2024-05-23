import geometry
from itertools import combinations

TestCases = int(input())
arr=[] 
for x in range(TestCases):
    arr.append(input())
    

# create each point relative to the top left

Points = []

for line in range(len(arr)):
    for values in range(TestCases):
        if(arr[line][values] != '.'):
            Points.append(geometry.Point(line,values))

Tripples = combinations(Points,3)
counter = 0
for x in Tripples:
    if(x[0].colinear(x[1], x[2])):
        counter +=1

print(counter)

