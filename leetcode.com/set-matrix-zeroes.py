from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        self.INF = 1e9+5
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.dfs(matrix, m,n,i,j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -self.INF:
                    matrix[i][j] = 0

    def dfs(self,matrix, m:int,n:int,i:int,j:int) -> None:
        for k in range(n):
            if matrix[i][k] != 0:
                matrix[i][k] = -self.INF
        for l in range(m):
            if matrix[l][j] !=0:
                matrix[l][j] = -self.INF

        

if __name__ == "__main__":
    s = Solution()
    a = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    s.setZeroes(a)
    print(a)
    a = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    s.setZeroes(a)
    print(a)

    a = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(a)
    print(a)#[[0,0,0,0],[0,4,5,0],[0,3,1,0]]