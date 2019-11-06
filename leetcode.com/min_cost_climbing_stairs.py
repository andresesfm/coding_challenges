import sys
from typing import List

INF = int(1e9+5)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      n = len(cost)
      DP = [INF]*(n+1)
      DP[0]=0
      DP[1]=0
      for i in range(2,n+1):
        DP[i] = min(DP[i-1]+cost[i-1],DP[i-2]+ cost[i-2])
      print(DP)
      return DP[n]




for line in sys.stdin:
  cost = [int(i) for i in line.split(',')]
print(cost)

solution = Solution()



print(solution.minCostClimbingStairs(cost))