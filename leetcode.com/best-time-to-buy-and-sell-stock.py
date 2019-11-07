import sys
from typing import List

INF = 1e9+5

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_purchase = INF
        max_profit = 0
        for i in range(n):
          min_purchase = min(min_purchase,prices[i])
          max_profit = max(max_profit, prices[i]-min_purchase)
        #print(min_purchase)
        return max_profit

for line in sys.stdin:
  prices = [int(i) for i in line.split(',')]

s = Solution()

print (s.maxProfit(prices))