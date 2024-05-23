Groups = {}
while(True):
    try:
        line = input().split()
        if (line[0] == ("group")):
            Groups[line[1]] = set(line[3:]) 

        else:
            stack = []
            # make a stack
            for x in line[::-1]:
                if x == "union":
                    first = stack.pop()
                    second = stack.pop()
                    #new set
                    stack.append(first.union(second))
                elif x == "intersection":
                    first = stack.pop()
                    second = stack.pop()
                    #new set
                    stack.append(first.intersection(second))
                    
                elif x == "difference":
                    first = stack.pop()
                    second = stack.pop()
                    #new set
                    stack.append(first.difference(second))
                else:
                    #push none operators onto stack
                    stack.append(Groups[x])
            Answer = []
            for x in stack[0]:
                Answer.append(x)
            Answer.sort()
            print(" ".join(Answer))

        #stuff
    except:
        break
