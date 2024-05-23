'''
Programmer: Miguel D. Wills
Program Purpose: TO SOLVE INTERGALTIC BIDDING
Date Written: 9/6/2023
'''
lines, lottery = input().split()

lines = int(lines)

lottery = int(lottery)

inputGiven = []

for x in range(0, lottery):
    name, bid  = input().split()
    inputGiven.append(bid)



# take in the inputs and sum their combination to see what combination equals
# the lottery number