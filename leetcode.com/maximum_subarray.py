import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        DP=[0]*(n)
        DP[0]=nums[0]
        for i in range(1,n):
          #DP[i] = max sum up to index i
          DP[i]= max(DP[i-1]+nums[i],nums[i])
        print(DP)
        return max(DP)

solution = Solution()

for line in sys.stdin:
  nums = [int(i) for i in line.split(',')]
  print(nums)

print(solution.maxSubArray(nums))