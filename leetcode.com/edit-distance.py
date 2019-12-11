class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        INF = 1e3+5
        DP = [[INF for j in range(l2+1)] for i in range(l1+1)]
        for i in range(l1+1):
            DP[i][0] = i
        for j in range(l2+1):
            DP[0][j] = j
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                c1 = word1[i-1]
                c2 = word2[j-1]
                if c1 == c2:
                    DP[i][j]= DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])+1
        for e in DP:
            print(e)
        return DP[l1][l2]

if __name__ == "__main__":
    s = Solution()
    print(s.minDistance(word1 = "horse", word2 = "ros"))#3
    print(s.minDistance(word1 = "intention", word2 = "execution"))#5
    print(s.minDistance("zoologicoarchaeologist","zoogeologist"))#10