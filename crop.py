from geometry import Point
from geometry import Triangle

iteration = int(input())

threshold = 1e-9


for x in range(iteration):
    n,A,B,C,D,X,Y,M = input().split()
    #print(n)

    array = []
    array.append(Point(int(X),int(Y)))
    for i in range(1,int(n)):
#        print(X)
        X = (int(A) * int(X) + int(B)) % int(M)
        Y = (int(C) * int(Y) + int(D)) % int(M)
        array.append(Point(X,Y))


    counter = 0
    for tree1 in array:
        for tree2 in array:
            for tree3 in array:

                if tree1 == tree2 or tree1 == tree3 or tree2 == tree3:
                    continue
                CenterPoint = (   (tree1.x + tree2.x + tree3.x)/3 ), ((tree1.y + tree2.y + tree3.y) / 3 )
                
                if (abs((CenterPoint[0] - round(CenterPoint[0]))) < threshold) and (abs((CenterPoint[1] - round(CenterPoint[1]))) < threshold):
                    counter = counter +1
                
    print(f"Case #{x+1}: {int(counter/6)}")                


