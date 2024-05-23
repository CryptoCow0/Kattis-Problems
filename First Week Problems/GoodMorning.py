#take first number then append 0 to the end
amount = int(input())
arr = []

for x in range(0, amount):
    current = str(input())
    arr.append(current)

#print(arr)
possible = {"1": "1234567890", "2" :"2356890", "3" : "369", "4" : "4567890", "5" : "56890", "6" : "69", "7": "7890", "8": "890", "9" : "9", "0":"0"}


s = []

# create every possible number

for x in possible:
    for j in possible[x]:
        for k in possible[j]:
            s.append(x)#create every number
            s.append(x+j)
            s.append(x+j+k)
            #print(x,x+j, x+j+k)


answers = []




# greedy search
for x in arr:   
    counter = 1
    while(True):
        if(x in s):
            print(x)
            break
        if(str(int(x) - counter) in s):
            print(int(x) - counter )
            break
        if(str(int(x) + counter ) in s):
            print(int(x) + counter)
            break

        counter +=1
        
