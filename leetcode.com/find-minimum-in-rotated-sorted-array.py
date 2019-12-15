from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n <1:
            return -1
        elif n ==1:
            return nums[0]
        elif n == 2:
            return min(nums[0],nums[1])
        l = 0
        r = n-1
        m = l + (r-l)//2
        INF=1e9+5
        minim = INF
        while l<=r:
            if nums[m]< minim:
                minim = nums[m]
            if nums[l]< nums[m] and nums[m]< nums[r]:#the full array is sorted (no rotation)
                return nums[l]
            if l == m or m == r:
                minim = min(minim, nums[l], nums[r]) 
                break
            if nums[l]<nums[m] and nums[r]<nums[m]:
                l = m
                r = r
                m = l + (r-l)//2
            elif nums[l]>nums[m] and nums[r]>nums[m]:
                minim =  min(minim, self.findMin(nums[:m+1]))
                break
            else:
                minim = -1
                print('unexpected')
                break
        return minim

def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))#1
    print(s.findMin([4,5,6,7,0,1,2]))#0
    print(s.findMin([2,1]))#1
    print(s.findMin([2,3,1]))#1