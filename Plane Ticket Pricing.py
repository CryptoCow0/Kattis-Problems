##DYNAMIC PROGRAMMING

seats , lines = input().split()

lines = int(lines) + 1
seats = int(seats)

cache = {}

Combination = []

for i in range(lines):
    current = input().split()
    #int(current)
    PT =[]
    for j in range(int(current[0])):
        PT.append([int(current[j+1]), int(current[int(current[0]) + j + 1])])
    Combination.append(PT)

#print(Combination)
start = 0

def solution(seats, weeks):
    global start

    if ((seats,weeks)) in cache: return cache[(seats,weeks)]

    if (weeks == 0): return 0

    if (seats == 0): return 0

    CurrentWeek = lines - weeks    
    
    summationList = []

    for i in range(len(Combination[CurrentWeek])):
        
        if (seats >= Combination[CurrentWeek][i][1]):

            NewSeats = seats - Combination[CurrentWeek][i][1] 
            summation = Combination[CurrentWeek][i][0] * Combination[CurrentWeek][i][1] + solution(NewSeats, weeks-1) 
            summationList.append([summation,Combination[CurrentWeek][i][0]])
        
        else:
            summation = Combination[CurrentWeek][i][0] * seats + solution(0, weeks-1)
            summationList.append([summation,Combination[CurrentWeek][i][0]]) 
            #seats = 0
    #print(summationList)
    
    balls = max(summationList, key = lambda x:x[0])
    
    cache[seats, weeks] = balls[0]
    
    start = balls[1]

    return balls[0]

    
print(solution(seats, lines))
print(start)
    