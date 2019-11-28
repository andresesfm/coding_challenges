from typing import List
import math

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        DP = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    DP[i][j] = int(matrix[i][j])
                else: 
                    if matrix[i][j] == "1":
                        DP[i][j] = min(DP[i-1][j-1],DP[i][j-1],DP[i-1][j])+ int(matrix[i][j])
                    else:
                        DP[i][j] = 0
        print('[')
        for r in DP:
            print(r)
        print(']')
        return pow(max(map(max,DP)),2)


if __name__ == "__main__":
    s = Solution()
    a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(s.maximalSquare(a))  # 4
    a = [["0","1"]]
    print(s.maximalSquare(a)) #1
    a = [["1","0"]]
    print(s.maximalSquare(a)) #1
    a= [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
    print(s.maximalSquare(a))
