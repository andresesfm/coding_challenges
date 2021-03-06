from typing import List
from typing import Set
from typing import Tuple
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                res =self.existR(board,word,i,j,0,set())
                if res:
                    return True
        return False
    def existR(self, board: List[List[str]], word: str, i:int,j:int,wi:int, visited:Set[Tuple]) -> bool:
        vkey = (i,j)
        if vkey in visited:
            return False
        else:
            visited = set(visited)
            visited.add(vkey)
        m =len(board)
        n = len(board[0])
        if word[wi] == board[i][j]:
            if wi == len(word)-1:
                return True
            else:
                for k,l in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if i+k < m and i+k >=0 and j+l< n and j+l >=0: 
                        res =self.existR(board,word,i+k,j+l,wi+1,visited)
                        if res:
                            return True
        return False


def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    board =[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    print(s.exist(board,'ABCCED'))#True
    print(s.exist(board,'SEE'))#True
    print(s.exist(board,'ABCB'))#False
    print(s.exist([["a","b"],["c","d"]],"acdb"))# true
    print(s.exist([["a","b"],["c","d"]],"abcd"))#false