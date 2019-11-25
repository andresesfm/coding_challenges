class Solution:
    def numTrees(self, n: int) -> int:
        DP = [0 for i in range(n+1)]
        if n ==0:
            return 0
        DP[0] = 1
        if n ==1:
            return 1
        DP[1] = 1
        #n = i-1+1+n-i
        for i in range(2,n+1):
            for j in range(i):
                DP[i] += DP[j] * DP[i-j-1]
        print(DP)
        return DP[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(4))