import sys
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==0:
          return 0
        DP = [0]*n
        #DP[i] is the max money at position i
        for i in range(n):
          if i==0:
            DP[i] = nums[0]
          elif i == 1:
            DP[i]=max(nums[0],nums[1])
          else:
            DP[i] = max(DP[i-2]+nums[i],DP[i-1])

        return DP[n-1]


if __name__ == "__main__":
    for line in sys.stdin:
        nums = [int(i) for i in line.split(',')]
    s = Solution()
    print(s.rob(nums))