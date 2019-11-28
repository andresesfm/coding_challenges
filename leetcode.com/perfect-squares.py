import math
class Solution:
    def numSquares(self, n: int) -> int:
        INF = 1e9+5
        DP = [INF for i in range(n+1)]
        if n == 0:
            return 0
        DP[0]=0
        if n == 1:
            return 1
        DP[1]=1
        if n == 2:
            return 2
        DP[2]=2
        for i in range(3,n+1):
            for j in range(1,int(math.sqrt(i))+1):
                DP[i] = min(DP[i],DP[i-pow(j,2)]+1)
        print(DP)
        return DP[n]

if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))#3
    print(s.numSquares(13))#2