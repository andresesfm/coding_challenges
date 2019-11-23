from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if n ==0:
            return False
        fits = True
        for w in wordDict:
            a = s
            if w in s:
                a = a.replace(w,'',1)
                assert len(a) < len(s)
                if len(a) > 0:
                    fits = fits or self.wordBreak(a,wordDict)
            else:
                fits = fits or self.wordBreak(a,list(filter(lambda x: x!=w ,wordDict)))
        return False

if __name__ == "__main__":
    s = Solution()
    #print(s.wordBreak('leetcode',["leet", "code"]))
    #print(s.wordBreak('applepenapple',["apple", "pen"]))
    #print(s.wordBreak('catsandog',["cats", "dog", "sand", "and", "cat"]))
    print(s.wordBreak("bb",["a","b","bbb","bbbb"]))