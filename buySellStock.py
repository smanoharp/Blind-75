from typing import List
def maxProfit(prices:List[int]) -> int:
    l = 0
    r = 1
    res = 0

    while(r < len(prices)):
        if (prices[l] < prices[r]):
            profit = prices[r] - prices[l]
            res = max(res, profit)
        else:
            l = r
        r += 1
    return res

testPrices = [10,1,5,6,7,1]
print(maxProfit(testPrices))