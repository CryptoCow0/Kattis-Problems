loops = int(input("Put int your loops "))
answer = []

for x in range(0, loops):
    # take in the number you are on and then take in the number to be converted


    skip, number = input().split()
    
    
    
    #print(number)
    
    numebr = str(number)    
    
    
    count = len(number)-1 # this will be the exponent
    #print(f"cout starts as {count}")
    octal = 0
    for x in number: #should go backwards
        #print(x)
        if(x == "9" or x == "8"):   
            octal = 0
            break #ends the for loop
        elif (count >= 0):
            octal += int(x) * pow(8,count)

            #print(octal)
            #print(f"count is {count}")
            count = count - 1
    #print(octal)
    


    hex = 0
    count = len(number)-1
    for x in number: #should go backwards
        #print(x)
        
        if (count >= 0):
            hex += int(x) * pow(16,count)

            #print(hex)
            #print(f"count is {count}")
            count = count - 1

    answer.append([int(skip),octal, int(number),hex])
    


for x in range(0, len(answer)):
    print(int(answer[x][0]), int(answer[x][1], answer[x][2], answer[x][3]))



    #skip the first number then do math