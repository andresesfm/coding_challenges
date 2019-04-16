class Solution:
    """
    Implementation of https://leetcode.com/problems/house-robber
    """
    def __init__(self):
        self.memo={}

    def rob(self, nums: List[int]) -> int:
        return self.robr(nums,0)
        
    def robr(self, nums: List[int], i: int) -> int:
        if len(nums[i:]) == 0:
            r =0
            self.memo[i]=r
            return r
        elif len(nums[i:]) == 1:
            r =nums[i]
            self.memo[i]=r
            return r
        elif len(nums[i:]) == 2:
            r =max(nums[i],nums[i+1])
            self.memo[i]=r
            return r
        
        if i+2 in self.memo:
            mi2 = self.memo[i+2]
        else:
            mi2 = self.robr(nums,i+2)
            self.memo[i+2] = mi2
            
        if i+1 in self.memo:
            mi1 = self.memo[i+1]
        else:
            mi1 = self.robr(nums,i+1)
            self.memo[i+1] = mi1
        return max(nums[i] + mi2, mi1)