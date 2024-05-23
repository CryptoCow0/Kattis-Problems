line = input()

Damaged = input().split()

Reserved = input().split()


#print(Reserved)
for x in Reserved:
    if x in Damaged:
        Damaged.remove(x)
    elif (str(int(x)-1)) in Damaged:
        Damaged.remove(str(int(x)-1))
       # print(x)
        #print(Damaged)
    elif(str(int(x)+1)) in Damaged:
        #print(x)
        Damaged.remove(str(int(x)+1))
        #Reserved.remove(x)
       # print(Damaged)
#print(Damaged)
print(len(Damaged))

