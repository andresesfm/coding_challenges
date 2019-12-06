from typing import List
class BottomUpTooManySpecialCasesSolution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        #base case(s):
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return 1 if abs(nums[0]) == abs(S) else 0
        if sum(nums) < S:
            return 0
        if S == 0:
            m = 0
            S = m
            nums = list(map(lambda x: x+m,nums))
        print(nums)
        DP = [[[0 for k in range(2)] for j in range(S+1)] for i in range(l+1)]
        #DP[i][j][k] = max count of adding/substracting element i to current sum 
        for i in range(1,l+1):
            current = nums[i-1]
            for j in range(S+1):
                for k in range(2):
                    if current ==0:
                        DP[i][j][k] = DP[i-1][j][k]*2 if DP[i-1][j][k] != 0 else 1
                    elif j<=S:
                        if i>=2 and nums[i-2]==0:
                            toSum = DP[i-1][j][k]
                        else:
                            toSum = current if k==0 else -current
                        DP[i][j][k] = max(DP[i-1][j][k],DP[i-1][j][k] +toSum)
                    else:
                        DP[i][j][k] = max(DP[i][j][k],DP[i-1][j][k])
        for i in range(len(DP)):
            print(DP[i])
        return max(DP[l][S][0],DP[l][S][1])

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        res = self.findHelper(nums,S,0)
        print(self.memo)
        return res

    def findHelper(self,nums:List[int],S: int, i: int) -> int:
        memokey = (len(nums)-i,S)
        if memokey in self.memo:
            return self.memo[memokey]
        if i >= len(nums):
            if S == 0:
                return 1
            else:
                return 0
        res = self.findHelper(nums,S+nums[i],i+1) + self.findHelper(nums,S-nums[i],i+1)
        self.memo[memokey] = res
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1],3))#5
    print(s.findTargetSumWays([1,0],1))#2
    print(s.findTargetSumWays([0,0,0,0,0,0,0,0,1],1))#256
    print(s.findTargetSumWays([1,2,1],0))
    print(s.findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],132))
