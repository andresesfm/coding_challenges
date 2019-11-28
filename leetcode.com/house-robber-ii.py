from typing import List

class KeepingTrackSolution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: 
            return 0
        DP  = [(0,False) for i in range(n)]#(best value,starts at element 0)
        DP[0] = (nums[0],True)
        if n == 1:
            return nums[0]
        DP[1] = (nums[1],False)
        for i in range(2,n):
            v_2,starts_2 =  DP[i-2]
            v_1,starts_1 = DP[i-1]
            if i != n-1:
                if v_1 > v_2+nums[i]:
                    DP[i] = DP[i-1]
                else:
                    DP[i] = (v_2 + nums[i],starts_2)
            else:
                if v_1 > v_2+nums[i] and not starts_1:
                    DP[i] = DP[i-1]
                elif not starts_2:
                    DP[i] = (v_2 + nums[i],starts_1)
                else:
                    DP[i]=(0,False)
        print(DP)
        return max(DP[n-2][0],DP[n-1][0])

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: 
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0],nums[1],nums[2])
        DP = [0 for i in range(n-1)]
        DP2 = [0 for i in range(n-1)]
        a = nums[1:]
        b = nums[:n-1]
        print(a)
        print(b)
        DP[0] = a[0]
        DP[1] = a[1]
        DP2[0] = b[0]
        DP2[1] = b[1]
        for i in range(2,n-1):
            DP[i] = DP[i-1]
            DP2[i] = DP2[i-1]
            for j in range(i-2,-1,-1):
                DP[i] = max(DP[i], DP[j] + a[i])
                DP2[i] = max(DP2[i], DP2[j] + b[i])
        print(DP)
        print(DP2)
        return max(DP[n-2], DP2[n-2])


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2,3,2]))#3
    print(s.rob([1,2,3,1]))#4
    print(s.rob([1,2,1,1]))#3
    print(s.rob([2,7,9,3,1]))#11
    print(s.rob([4,1,2,7,5,3,1]))#14