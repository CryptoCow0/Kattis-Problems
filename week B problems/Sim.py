backspace = input()

out = []

for c in range(len(backspace)):

    if backspace[c] != '<': out.append(backspace[c])

    else:
        out.pop()
        
        # this is o(n) out = out[:-1]



print ("".join(out))