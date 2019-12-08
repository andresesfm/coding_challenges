from typing import List
class NotWorkingSolution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                res = max(res,self.DFS(i,j,grid))
        return res
        
    def DFS(self,i: int, j: int,grid: List[List[int]])-> int:
        if i > len(grid)-1 or j > len(grid[i]):
            return 0
        if grid[i][j] == 0:
            return 0
        offset = 1
        while i+offset<len(grid) and j+offset < len(grid[i]) and grid[i][j+offset] == 1 and grid[i][j+offset]==1:
            offset +=1
        # while offset>1 and (i+offset>len(grid)-1 or j+offset>len(grid[i])-1 or grid[i+offset][j+offset] == 0  ):
        #     offset -=1
        return offset * offset

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        DP = [[[0,0] for j in range(n+1)] for i in range(m+1)]#[len from top, len from left]
        DP[0][0] = [grid[0][0]]*2
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i-1][j-1]== 1:
                    DP[i][j] = [DP[i-1][j][0]+1 , DP[i][j-1][1]+1]
                else:
                    DP[i][j] = [0,0]
                l = min(DP[i][j][0],DP[i][j][1])
                k = l
                while k > res:
                    ll = min(DP[i-k+1][j][1],DP[i][j-k+1][0])
                    if ll>=k:
                        res = max(res,k)
                        #print(res, i,j,l,k)
                    k-=1
        for i in range(len(DP)):
            print(DP[i])
        return res*res

if __name__ == "__main__":
    s = Solution()
    print(s.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))#9
    print(s.largest1BorderedSquare([[1,1,0,0]]))#1
    print(s.largest1BorderedSquare([[0,1],[1,1]]))#1