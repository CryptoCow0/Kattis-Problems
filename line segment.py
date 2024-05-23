import geometry
TestCases = int(input())
OutPut = []
for x in range(TestCases):
    Values = input()
    ValuesList = Values.split()    
    Xone, Yone, Xtwo, Ytwo, Xthree, Ythree, Xfour, Yfour = map(float, ValuesList)

        
    Points = {
        Xone: Xtwo,
        Xtwo: Xone,
        Xthree: Xfour,
        Xfour: Xthree,
        Yone: Ytwo,
        Ytwo: Yone,
        Ythree: Yfour,
        Yfour: Ythree

    } 
    
    smallestX = Xone
    smallestY = Yone
    for x in range(0, len(ValuesList),2):
        if (float(ValuesList[x]) < smallestX):
            smallestX = float(ValuesList[x])
            smallestY = float(ValuesList[x+1])

    
                 
    LineOne = geometry.Line.fromPoints(smallestX,smallestY,Points[smallestX], Points[smallestY])
    Points.pop(smallestY)
    Points.pop(smallestX)

    newX = 0
    newY = 0
    # Iterating through keys and values
    for key, value in Points.items():
        for values in range(ValuesList):
            if (float(ValuesList[values]) == key):
                newX = key
                newY = float(ValuesList[values + 1 ])

        
    #whatever is left?
    #how to determine what is left
    LineTwo = geometry.Line.fromPoints(newX, newY, Points[newX], Points[newY])
    
    #sorting / making the points so that X-one is always the left most point
       
    
    lineOne = geometry.Line.fromPoints(geometry.Point(Xone,Yone), geometry.Point(Xtwo,Ytwo))
    lineTwo = geometry.Line.fromPoints(geometry.Point(Xthree,Ythree), geometry.Point(Xfour,Yfour))


    if(lineOne.isSameAs(lineTwo) == False):
        # do the bounds checking
        # we want to ensure that the intersection is within the points
        # sort the points so that Xone is alwyas the furthest point left
        try:
            xPoint = lineOne.intersectAt(lineTwo).x
            yPoint = lineOne.intersectAt(lineTwo).y
            
            if(Xone < xPoint and Xtwo > xPoint and Xthree < xPoint and Xfour > xPoint):
                OutPut.append(lineOne.intersectAt(lineTwo))
                OutPut.append(lineTwo.intersectAt(lineOne))
        except:
            OutPut.append("none")    
        


for answer in OutPut:
    try:
        print(f"{answer.x:.2f}, {answer.y:.2f}")
    except:
        print("none")
    
        #Degenerate cases


    '''
    line sgement.

edge cases:



make the lines

is parrllel:


find y intercepts if parrlel and if not the same then line segments don't ineresect else




if (l1.sameAs(l2)):
the overlap is always one of the four points given such that p1 is always left to p2 and p3 is left p4

if you sort the points then osrt hte lines 
start will always be be p3
end will be min (p2, p4)

if start == end
print(start)

else
print(start,end)

    '''

    
    #create lines?








