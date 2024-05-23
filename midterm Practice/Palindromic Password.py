N = input()

arr = []
for x in range(int(N)):
    current = input()
    #if a palindrome
    if(current == current[::-1]):
        arr.append(current)
    else:
            
        PalFound = False
        length = len(current)
        middle = length //2
        left_half = current[:middle + length % 2]

        testP1 = int(left_half + left_half[-(length //2):][::-1])

        left_halfincrease = str(int(left_half)+1)

        testP2 = int(left_halfincrease + left_halfincrease[-(length //2):][::-1])

        left_halfdecrease = str(int(left_half) -1)
        if left_halfdecrease:
            testP3 = int(left_halfdecrease + left_halfdecrease[-(length //2):][::-1])
        else:
            testP3 = int(left_halfdecrease + left_halfdecrease[::-1])
        closest_palindrome = min(testP1, testP2, testP3, key=lambda x: abs(x - int(current)))
        arr.append(closest_palindrome)

for x in range(len(arr)):
    print(arr[x])