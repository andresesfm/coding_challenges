from typing import List

class QuadraticSolution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        DP =[[0 for i in range(n)] for j in range(n)]
        if n == 0:
            return 0
        DP[0][0] = nums[0]
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    DP[i][j] = nums[i]
                else:
                    DP[i][j] = DP[i][j-1] * nums[j]
        print(DP)
        return max(map(max,DP))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        DP = [0 for i in range(n)]
        DP2 = [0 for i in range(n)]
        if n == 0:
            return 0
        DP[0] = nums[0]
        for i in range(1,n):
            DP[i] = max(DP[i-1] * nums[i], DP2[i-1]*nums[i], nums[i])
            DP2[i] = min(DP[i-1] * nums[i],DP2[i-1]* nums[i],nums[i])
        print(DP)
        return max(DP)


if __name__ == "__main__":
    s = Solution()

    print(s.maxProduct([2,3,-2,4]))#6

    print(s.maxProduct([-2,0,-1]))#0

    print(s.maxProduct([-2,3,-4]))#24