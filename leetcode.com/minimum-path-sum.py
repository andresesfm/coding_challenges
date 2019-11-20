import sys
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = 1e9+5
        M = len(grid)
        N  = len(grid[0])
        DP = [[INF for j in range(N)] for i in range(M)]
        DP[0][0]= grid[0][0]
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                top = INF
                if i>0:
                    top = DP[i-1][j]
                left = INF
                if j>0:
                    left = DP[i][j-1]
                DP[i][j] = min(top,left)+ grid[i][j]
        return DP[M-1][N-1]


if __name__ == "__main__":
    line_count = 0
    for line in sys.stdin:
        if line_count == 0:
            M,N = [int(i) for i in line.split(',')]
            G = [[] for i in range(M)]
        else:
            G[line_count-1] = [int(i) for i in line.split(',')]
        line_count+=1
    print(G)
    s = Solution()
    print(s.minPathSum(G))