from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = l + (r-l)//2
        while l<=r:
            if nums[m] == target:
                return m
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            elif l ==r or l ==m or r == m:
                return-1
            
            if nums[l] <= nums[m] and nums[m] <= nums[r]:#sorted case
                if target> nums[m]:
                    l = m
                    r = r
                    m = l +(r-l)//2
                    continue
                elif target< nums[m]:
                    l = l
                    r = m
                    m = l +(r-l)//2 
                    continue
                else:
                    return m

            if nums[m]> nums[r] and nums[m]> nums[l]:
                if nums[m]>=target and target>=nums[l]:
                    l = l
                    r = m
                    m = l +(r-l)//2
                else:
                    res = self.search(nums[m:],target)
                    return m + res if res != -1 else -1
            elif nums[m]< nums[r] and nums[m]< nums[l]:
                if nums[m]<=target and target<=nums[r]:
                    l = m
                    r = r
                    m = l +(r-l)//2
                else:
                    res = self.search(nums[:m],target)
                    return res
            else:
                print('unexpected')
                return-1
        return -1



def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    # print(s.search(nums = [4,5,6,7,0,1,2], target = 0))#4
    # print(s.search([4,5,6,7,0,1,2], target = 3))#-1
    # print(s.search([1],1))#0
    # print(s.search([1,3],3))#1
    # print(s.search([4,5,6,7,0,1,2],6))#2
    print(s.search([1,3],2))#?