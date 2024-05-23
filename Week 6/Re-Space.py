Line = str(input("something"))

dictionary = str(input().split())

def recursion(n):
    if len(n) == 0:
        return 0, ""
    
    #bestCost = len(n), bestSPlit = s
    bestCost = 10
    for i in range(len(n)):
        left = n[:i] 
        right = (n[i:-1])
        cost = CalcCost(left) + recursion(n).left()
    
        if cost < bestCost:
            return cost, left + " " + recursion(right).right()
    
def CalcCost(s):
    if (s in dictionary):
        return 0
    else:
        return len(s)


recursion(Line)

