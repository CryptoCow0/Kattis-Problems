import re

# regular expression to find every hex number by 0(x either capital or lowercase) /d is digits 0-9 A-Fa-f is evey letter A-F
pattern = r'0([X]|[x])([\dA-Fa-f]+)'

#0[x|X][\dA-Fa-f]+

while(True):
    try:
        line = input()
        Hex = re.findall(pattern, line)
        array = []
        for x in Hex:
            Answer = int(x[1], 16)
            print( "0"+x[0]+x[1], Answer)
        
    except:
        break
