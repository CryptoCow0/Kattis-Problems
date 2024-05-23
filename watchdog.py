import geometry
TestCases = int(input())

for x in range(TestCases):
    S, H = input().split()
    S = int(S)
    H = int (H)
    

    hatches = []
    for Coords in range(H):
        x , y = input().split()
        hatches.append(geometry.Point(float(x), float(y)))
    possibleleash = []

    for i in range(1,S):
        for j in range(1,S):
            NotHatch = True
            if geometry.Point(i,j) in hatches:
                continue
            radipossible = [i,j, S-i, S-j]
            Circ = geometry.Circle(geometry.Point(i,j), min(radipossible))

            
            for hatche in range(len(hatches)):
                if (Circ.containsPoint(hatches[hatche]) == -1):
                    NotHatch = False
                    break
            if(NotHatch):
                possibleleash.append((i,j))
    
    if(len(possibleleash) ==0 ):
        print("poodle")
    else:
        answer = min(possibleleash)
        print(f"{answer[0]} {answer[1]}")

