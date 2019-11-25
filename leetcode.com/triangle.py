from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INF = 1e9+5
        n = len(triangle)
        if n == 0: 
            return 0
        if len(triangle[0]) == 0:
            return 0 
        DP = [0 for i in range(n)]
        DP[n//2-1]= triangle[0][0]
        if n >1:
            DP[n//2] = triangle[0][0]
        offset = n //2 -1
        #print(DP)
        for i in range(1,len(triangle)):
            DP2 = DP[:]#clone DP to prevent cross-contamination
            l = len(triangle[i])
            for k in range(l):
                j = k+offset
                if k<=0:
                    upleft = INF
                else:
                    upleft =  DP2[j]
                if k == l-1:
                    upright= INF
                else:
                    upright = DP2[j+1]

                DP[j] = min(upleft,upright)+triangle[i][k]
            offset-=1
            #print(DP)
        return min(DP)

if __name__ == "__main__":
    arg = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
        ]
    s = Solution()
    print(s.minimumTotal(arg))

    arg = [
        [-1],
        [3,2],
        [-3,1,-1]
        ]
    print(s.minimumTotal(arg)) #expected -1