import sys
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, G: List[List[int]]) -> int:
        M = len(G)
        N = len(G[0])

        DP = [[0 for j in range(N)] for i in range(M)]
        if G[0][0] == 1:
            DP[0][0] = 0
        else:
            DP[0][0] = 1
        for i in range(M):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if G[i][j] ==1:
                    DP[i][j] = 0
                    continue
                top = 0
                if i>0:
                    top = DP[i-1][j]
                left = 0
                if j>0:
                    left = DP[i][j-1]
                DP[i][j] = top + left
        print(DP)
        return DP[M-1][N-1]


if __name__ == "__main__":
    line_count = 0
    for line in sys.stdin:
      if line_count ==0:
        M,N = [int(i) for i in line.split(',')]
        G = [[] for j in range(M)]
      else:
        G[line_count-1]= [int(i) for i in line.split(',')]
      line_count +=1
    print(G)
    s = Solution()
    print(s.uniquePathsWithObstacles(G))
