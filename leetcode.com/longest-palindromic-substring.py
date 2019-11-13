import sys
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #DP[i] is the longest palindrome len up to index i
        n = len(s)
        if n ==1:
            return s
        DP = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            DP[i][i] = 1
        lpali = ""
        for i in range(n-1):
            j = i + 1
            if s[i] == s[j]:
                    DP[i][j] = 1
        print(DP)
        for k in range(2,n):
            for i in range(n-1):
                j = i+k
                if j < n:
                    if s[i] == s[j] and DP[i+1][j-1] == 1:
                            DP[i][j] = 1
                    else:
                            DP[i][j] = 0
        for i in range(n):
            for j in range(n):
                if DP[i][j]==1:
                    if ((j-i+1) >= len(lpali)):
                        lpali = s[i:j+1]
                        print(lpali)
        print(DP)
        return lpali


if __name__ == "__main__":
    for line in sys.stdin:
      pali = line
    s = Solution()
    print(s.longestPalindrome(pali))