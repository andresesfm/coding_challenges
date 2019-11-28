from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        DP = [(0,0) for i in range(n)]#(max profit to this day holding 0 stock, max profit holding 1 stock)
        DP[0] = (0,-prices[0])
        DP[1] = (max(prices[1] - prices[0],0),max(-prices[0],-prices[1]))
        
        for i in range(2,n):
            DP[i] = (max(DP[i-1][1] + prices[i],DP[i-1][0]),
                    max(DP[i-2][0]-prices[i],DP[i-1][1]))

        print(DP)
        return(max([a[0] for a in DP]))

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]))#3