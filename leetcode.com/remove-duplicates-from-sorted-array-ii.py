from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lastIndex = 0
        i = 1
        while i<len(nums):
            if nums[i] == nums[lastIndex]:
                if lastIndex == 0:
                    lastIndex +=1
                    i+=1
                elif nums[lastIndex] == nums[lastIndex-1]:
                    i += 1
                else:
                    lastIndex+=1
                    nums[lastIndex] = nums[i]
                    i+=1
            else:
                lastIndex+=1
                nums[lastIndex] = nums[i]
                i+=1
            print(nums)
        return lastIndex+1


def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))#5/ 1, 1, 2, 2 and 3
    print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))#7/ 0, 0, 1, 1, 2, 3 and 3
    #print(s.())