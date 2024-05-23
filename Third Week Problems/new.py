import re
string = input()

pattern = '(^| ) (\w\d{2}) ($| )'
result = re.sub(pattern, ' *** ', string)

print(result.strip())


#Problem statement:
