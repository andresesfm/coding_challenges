from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n  = len(nums)
        if n == 0: 
            return 0
        DP = [0 for i in range(target+1)]
        DP[0]= 1
        for i in range(1,target+1):
            for j in range(n):
                if i-nums[j]>=0:
                    DP[i] =( DP[i]+ DP[i-nums[j]])
        print(DP)
        return DP[target]

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([1, 2, 3],4))#7