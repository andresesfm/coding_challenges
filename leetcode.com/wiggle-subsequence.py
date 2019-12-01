from typing import List
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        DP= [[1,1,1] for i in range(n)]#[up,down,equal]
        DP[0][0] = 1
        DP[0][1] = 1
        DP[0][2] = 1
        if n == 1:
            return 1
        if nums[0] == nums[1]:
            DP[1][2] = 1
        elif nums[0]>nums[1]:
            DP[1][1] = 2
        else:
            DP[1][0] = 2
        if n == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        for i in range(2,n):
            for j in range(i):
                if nums[j] == nums[i]:
                    DP[i][2] = max(DP[i][2],DP[j][2])
                elif nums[j]>nums[i]:
                    DP[i][1] = max(DP[i][1],DP[j][0]+1)
                elif nums[j]<nums[i]:
                    DP[i][0] = max(DP[i][0],DP[j][1]+1)
        print(DP)
        return max(DP[n-1][0],DP[n-1][1], DP[n-1][2])

if __name__ == "__main__":
    s = Solution()
    print(s.wiggleMaxLength([1,7,4,9,2,5]))#6
    print(s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))#7
    print(s.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))#2
    print(s.wiggleMaxLength([0,0,0]))#1
    print(s.wiggleMaxLength([3,3,3,2,5]))#3
    print(s.wiggleMaxLength([126,37,130,225,239,77,235,333,30,69,294,128,163,17,224,229,128,59,205,265,328,259,337,93,354,316,309,67,36,88,133,359,8,335,247,209,279,94,41,62]))
#25