from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if n == 0:
            return 0
        INF = 1e9+5
        DP =[INF for j in range(amount+1)]
        #base case 0 coins
        DP[0] = 0
        for i in range(1,amount+1):
            for j in range(n):
                if i>=coins[j]:
                    DP[i] = min(DP[i],DP[i-coins[j]]+1)
        print(DP)
        if DP[amount] == INF:
            return -1
        return DP[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5],11))#3
    print(s.coinChange([2],3))#-1