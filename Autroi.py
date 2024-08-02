string = input("Enter the name: ")
v = []
x = 0
for l in string:
#check if the string's letter is uppercase
	if l == '-':
		l = l + 1
		v.append(l)
		x = x + 1
print(v)
