import sys
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(matrix)==0 or len(matrix[0])==0:
            return
        N = len(matrix)
        M = len(matrix[0])
        DP = [[0 for i in range(M)] for j in range(N)]
        DP[0][0] =  matrix[0][0]
        for i in range(N):
            for j in range(M):
                if i>0 and j>0:
                    DP[i][j] = DP[i][j-1]+DP[i-1][j] - DP[i-1][j-1]+ matrix[i][j]
                elif i>0:
                    DP[i][j] = DP[i-1][j] + matrix[i][j]
                elif j>0:
                    DP[i][j] = DP[i][j-1] + matrix[i][j]
        printM(DP)
        self.DP = DP

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        DP = self.DP
        s = 0
        if row1 >0:
            s+= - DP[row1-1][col2]
        if col1 >0:
            s+= - DP[row2][col1-1]
        if row1>0 and col1>0:
            s+= DP[row1-1][col1-1]
        return DP[row2][col2] + s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#matrix
def printM(M):
  print('[')
  for row in M:
    print(row)
  print(']')

line_count=0
if __name__ == "__main__":
    for line in sys.stdin:
      if line_count == 0:
        N= int(line)
        M = [[] for i in range(N)]
      else:
        M[line_count-1]= [int(i) for i in line.split(',')]
      line_count+=1
    printM(M)

    s = NumMatrix(M)
    #print(s.sumRegion(0,0,0,0))
    #print(s.sumRegion(1,1,1,1))
    #print(s.sumRegion(0,0,1,1))
    #print(s.sumRegion(0,1,1,1))
    #print(s.sumRegion(2, 1, 4, 3))
    #print(s.sumRegion(1, 1, 2, 2))
    #print(s.sumRegion(1, 2, 2, 4))
    print(s.sumRegion(0,0,0,0))
    print(s.sumRegion(0,0,0,1))
    print(s.sumRegion(0,1,0,1))
