prices = [7,6,4,3,1]

if len(prices) <= 1: print(0)

ans, i = 0, 0
while i + 1 < len(prices):
    if prices[i] < prices[i + 1]:
        buy = prices[i]
        while i + 1 < len(prices) and prices[i] < prices[i + 1]:
            i += 1
        ans += prices[i] - buy
    i += 1
        
print(ans)