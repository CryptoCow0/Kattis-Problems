from itertools import permutations

x = input()
permSet = set(permutations(x))

x = int(x)
for p in permSet:
    perm = [''.join(p)]


min = int(''.join(perm[0]))

special = False
for j in range(0,len(perm)-1):
    #print(perm[j])
    if (min > int(''.join(perm[j])) and int(''.join(perm[j])) > x):
        #print("balls")
        min = int(''.join(perm[j]))
        special = True

if (special == True):
    print(min)
    #print("MIN WAS PRINTED")

if (not special):
    print(0)