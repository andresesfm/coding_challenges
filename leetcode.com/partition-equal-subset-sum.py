from typing import List
## base cases:
## [],[a] => False
## [a,b] => a == b
## [a,b,c] => a == b+c or a+b = c or a+c = b <==> a -b-c == 0 or a+b-c ==0 or a-b+c==0
## [a,b,c,d] => a == b+c+d or a+b == c+d or a+c == b+d or a+d = b+c or b == a+c+d or c == a+b+d or d == a+b+c
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if n <2:
            return 0
        if total %2 != 0:
            return False
        target = total //2
        DP = [[False for i in range(target+1)] for j in range(n) ]#[index in nums,cumulative sum]
        
        for i in range(n):
            DP[i][0] = True
        
        for s in range(1,target+1):
            DP[0][s] = nums[0] == s

        
        for i in range(n):
            for s in range(target+1):
                if DP[i-1][s]:
                    DP[i][s] = DP[i-1][s]
                elif s >= nums[i]:
                    DP[i][s] = DP[i-1][s-nums[i]]
        print(DP)
        return DP[n-1][target]

if __name__ == "__main__":
    s= Solution()
    print(s.canPartition([1, 5, 11, 5]))#true
    print(s.canPartition([1, 2, 3, 5]))#false