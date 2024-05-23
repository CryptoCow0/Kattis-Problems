import geometry
'''
make a circle of N, check if the area is less than or equal to A

Output:
Impossible
'''
A, N = input().split()
pi = 3.14159
b = geometry.Circle(c=(0,0),r=abs(float(N)/(2*pi)))

threshold = 1e-9


if (b.area() >= float(A)):
    print("Diablo is happy!")



    #abs((CenterPoint[0] - round(CenterPoint[0]))) < threshold)
else:
    print("Need more materials!")