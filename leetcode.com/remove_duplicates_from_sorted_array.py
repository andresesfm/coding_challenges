from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastOrdered = 0
        nextUnique = lastOrdered + 1
        l = len(nums)
        while True:   
            while nextUnique<l and nums[nextUnique] == nums[lastOrdered]:
                nextUnique +=1
            if lastOrdered != nextUnique and nextUnique < l:
                self.swap(nums,lastOrdered+1,nextUnique)
                lastOrdered += 1
                nextUnique += 1
            else:
                break
        return lastOrdered + 1
    
    def swap(self, nums: List[int], a: int, b: int)-> None:
        nums[a], nums[b] = nums[b],nums[a]

s = Solution()
#     LastO  NUnique
#     v       v             
#1 = [1,1,1,1,2,2,2,2,4,5]
#     LastO  NUnique
#       v     v             
#1 = [1,2,1,1,2,2,2,2,4,5]
#     LastO  NUnique
#       v       v      
l1 = [1,1,1,1,2,2,2,2,4,5]
i = s.removeDuplicates(l1)
print(i)
print(l1)
