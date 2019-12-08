from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if(len(board) != 9 or len(board[0]) !=9):
            return False
        DPv = [set() for j in range(9)]#vertical
        DPh = [set() for j in range(9)]#horizontal] 
        DP2 = [[set() for j in range(3)] for i in range(3)] #3x3 squares

        for i in range(9):
            for j in range(9):
                e = board[i][j]
                if e == '.':
                    continue
                
                if e in DPh[i] or e in DPv[j] or e in DP2[(i)//3][(j)//3]:
                    # print(e)

                    # print(DPv)
                    # print(DPh)
                    # for i in DP2:
                    #     print(i)
                    return False
                 
                DPh[i].add(e)
                DPv[j].add(e)
                DP2[i//3][j//3].add(e)
        
        # print(DPv)
        # print(DPh)
        # for i in DP2:
        #     print(i)
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))#true
    print(s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))#false