import re

text1 = "91193"
text2 = "0911"

pattern = r'\b911'

match1 = re.search(pattern, text1)
match2 = re.search(pattern, text2)

if match1:
    print("Match found in text1:", match1.group())
else:
    print("No match found in text1")

if match2:
    print("Match found in text2:", match2.group())
else:
    print("No match found in text2")
