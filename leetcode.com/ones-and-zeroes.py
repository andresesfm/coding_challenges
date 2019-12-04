from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        if l == 0:
            return 0
        DP = [[ [0 for i in range(n+1)] for j in range(m+1)] for k in range(l+1)]
        #DP[i][j][k] is the max number of strings we can include in the ith element, with j 0's and k 1's remaining

        for i in range(1,l+1):
            zeros = strs[i-1].count('0')
            ones = len(strs[i-1])- zeros
            for j in range(m+1):
                for k in range(n+1):
                    if zeros <=j and ones <= k:
                        DP[i][j][k] = max(DP[i-1][j][k], DP[i-1][j-zeros][k-ones]+1)
                    else:
                        DP[i][j][k] = DP[i-1][j][k]
        for i in range(len(DP)):
            print(DP[i])
        return DP[l][m][n]

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"],5,3))#4
    print(s.findMaxForm(["10", "0", "1"],1,1))#2