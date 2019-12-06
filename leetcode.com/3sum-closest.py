from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # base case(s):
        # if nums is less than three element long, then error out?
        # If len(nums) is 3 then return the sum
        # if len(nums) is 4 then return max(sum_{i=0,3}(^i))
        l = len(nums)
        if l <3:
            return 0 ##error out?

        nums  = sorted(nums)
        closest = nums[0] +nums[1] + nums[2]
        farthest = 0
        for i in range(l):
            left = i+1
            right = l-1
            while(left<right):
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target)< abs(closest -target):
                    closest = s
                if s == target:
                    return s
                elif s < target:
                    left +=1
                else:
                    right -=1
        return closest



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4],1))#2