from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0 for i in range(n)]
        if n == 0:
            return 0
        DP[0] = nums[0]
        for i in range(1,n):
            DP[i] = max(DP[i-1] * nums[i],nums[i])
        print(DP)
        return max(DP)


if __name__ == "__main__":
    s = Solution()

    print(s.maxProduct([2,3,-2,4]))#6

    print(s.maxProduct([-2,0,-1]))#0