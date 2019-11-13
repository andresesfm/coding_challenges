class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = [[0 for j in range(n)] for i in range(m)]
        DP[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i ==0 and j ==0:
                    continue
                top = 0
                if j>0:
                    top = DP[i][j-1]
                left = 0
                if i > 0:
                    left = DP[i-1][j]
                DP[i][j] = top+left 
        print(DP)
        return DP[m-1][n-1]


if __name__ == "__main__":
    s = Solution()
    m =3
    n= 2
    out = 3

    actual_out = s.uniquePaths(m,n)
    print(actual_out)
    assert actual_out == out

    m =7
    n= 3
    out = 28
    actual_out = s.uniquePaths(m,n)
    print(actual_out)
    assert actual_out == out