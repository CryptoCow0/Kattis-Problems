import geometry
TestCases = int(input())

for x in range(TestCases):
    #print(x)
    array = []
    X, Y = input().split()
    A = geometry.Point(float(X), float(Y))
    
    for y in range(int(input())):
        CandleX, CandleY = input().split()
        array.append(geometry.Point(float(CandleX), float(CandleY)))
    candle = False
    for Candle in array:
        
        if Candle.distance(A) < 8.0:
            print("light a candle")
            candle = True
            break
        
    if candle == False:
        print("Curse the darkness") 
        #Candle = 
