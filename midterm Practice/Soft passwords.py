S = input()
P = input()

if (P==S):
    print("Yes")
    quit()
else:
    if (S.lower() == P.lower()):
            print("Yes")
            quit()
    for x in range(10):
        if (S == str(x)+P):
            print("Yes")
            quit()
        if (S == P+str(x)):
            print("Yes")
            quit()
    print("No")


