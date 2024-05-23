import geometry

TestCases = int(input())
center = geometry.Point(0,0)
radii = []
for i in range(10):
    radii.append((i+1) * 20)


for test in range(TestCases):    
    DartThrows = int(input())
    DartList = []
    points = 0
    for Dart in range(DartThrows):
        x,y = input().split()
        DartList.append(geometry.Point(float(x),float(y)))

    for dart in DartList:
        distance =  center.distance(dart)
        for radi in radii:
            if distance <= radi:
                points+=1

    print(points)

