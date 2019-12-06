class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        mat = [ ['' for j in range((l))] for i in range(numRows)]
        y,x = 0,0
        dy,dx = 0,1
        for i in range(l):
            mat[y][x] = s[i]
            if numRows ==1:
                dy,dx = 0,1
            elif y == 0:
                dy,dx = 1,0
                #k remains the same
            elif y == numRows-1:
                dy,dx = -1,1
            y = y+dy
            x = x+dx
        res = ''
        #print(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]:
                    res+=mat[i][j]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING",3))#PAHNAPLSIIGYIR
    print(s.convert("PAYPALISHIRING",4))#PINALSIGYAHRPI
    print(s.convert("AB",1))