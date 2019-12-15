from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        mx = 0
        DP = [0 for j in range(n)]
        for i in range(m):
            if i == 0:
                DP = [int(matrix[i][j])for j in range(n)]
            else:
                for j in range(n):
                    if matrix[i][j] =='1':
                        DP[j] =  DP[j]+1
                    else:
                        DP[j] = 0
            mx = max(mx,self.histogramMax(DP))
            print(DP)
            print(mx)
        return mx
    
    def histogramMax(self, h)-> int:
        res = 0
        st =[]
        i = 0
        while i < len(h):
            if not st or h[st[-1]]<=h[i]:
                st.append(i)
                i +=1
            else:
                top = st.pop()
                if not st:
                    area = h[top] * i
                else:
                    area = h[top]*(i-st[-1]-1)
                res = max(res,area)

        while st:
            top = st.pop()
            if not st:
                area = h[top] * i
            else:
                area = h[top]*(i-st[-1]-1)
            res = max(res,area)
        return res

            



def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]))#6
    print(s.maximalRectangle([["1"]]))
    print(s.maximalRectangle([["0","1"]]))