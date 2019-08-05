"""
Accepted solution: https://leetcode.com/problems/remove-element
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr = 0
        last = len(nums)-1
        while curr<=last:
            if nums[last] == val:
                last -=1
                continue
            if nums[curr] == val:
                #swap
                nums[curr] = nums[last]
                last -=1
            else:
                curr+=1
        return curr

s = Solution()
l = [1,2,3,4,5]
r = s.removeElement(l,3)
print(l,r)