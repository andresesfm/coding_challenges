from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        DP = [False for i in range(n+1)]

        for i in range(1,n+1):
            for w in wordDict:
                wl = len(w)
                if wl<i and w == s[i-wl:i]:
                    DP[i] = DP[i] or DP[i-wl]
                elif w == s[:i]:
                    DP[i] = True
        print(DP)
        return DP[n]

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak('leetcode',["leet", "code"]))
    print(s.wordBreak('applepenapple',["apple", "pen"]))
    print(s.wordBreak('catsandog',["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak("bb",["a","b","bbb","bbbb"]))