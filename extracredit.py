from collections import defaultdict

#first, second = input().split()
#print('')
MODULUS = 1_000_000_007


def meaning(w,d,i,n,memory = {}):
    if i > n:
        return 1
    if i not in memory:
        s=0
        for each, k in d[w[i]].items():
            if w[i:].startswith(each):
                s = (s + k * meaning(w,d,i+len(each),n,memory)) % MODULUS

        memory[i] = s
    #print(memory[i])
    return memory[i]



number, word = input().split()
dictionary = defaultdict(dict)



for x in range(int(number)):
    first , second = input().split()

    dictionary[first[0]][first] = int(second)

print(meaning(word,dictionary,0, len(word)-1))