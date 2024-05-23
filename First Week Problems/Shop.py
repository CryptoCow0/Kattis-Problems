lenth = int(input())
prices = input().split()
#print(prices)
for x in prices:
    x = int(x)

prices.sort(reverse = True)

#print(prices)


position = 2
price = 0
while(position < lenth):
    
    price += int(prices[position])
    position += 3

print(price)