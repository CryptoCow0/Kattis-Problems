def count_ways_to_glue(n):
    # Create a list to store the number of ways to glue each length up to n
    total = [] 
    for x in range(n+1):
        total.append(0)
    #print(total)

    total[0] = 1
    # Loop through all possible lengths from 1 to n
    for i in range(1, n + 1):
        # You can glue a 1-meter piece to form a plank of length i
        if i >= 1:
            total[i] += total[i - 1]
            #print(total)
        # You can glue a 2-meter piece to form a plank of length i
        if i >= 2:
            total[i] += total[i - 2]
           # print(total)

        # You can glue a 3-meter piece to form a plank of length i
        if i >= 3:
            total[i] += total[i - 3]
            #print(total)

    return total[n]

# Input the desired length of the plank
n = int(input())
amount = count_ways_to_glue(n)
print(amount)
