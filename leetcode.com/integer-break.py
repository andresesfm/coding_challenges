class Solution:
    def integerBreak(self, n: int) -> int:
        if n ==0:
            return 0
        DP = [0 for i in range(n+1)]
        DP[0] = 0
        DP[1] = 1
        DP[2] = 1
        for i in range(3,n+1):
            for j in range(1,i):
                DP[i] = max(DP[i], DP[j] *(i-j),j *(i-j) )
        print(DP)
        return DP[n]
        

if __name__ == "__main__":
    s = Solution()
    #print(s.integerBreak(2))#1
    print(s.integerBreak(10))#36