from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        return self.helper(digits,len(digits)-1)
        
    def helper(self, digits: str, i: int) -> List[str]:
        #base case if digits is empty then return []
        if i < 0:
            return []
        combs = []
        prev = self.helper(digits,i-1)
        for e in self.phone[digits[i]]:
            if not prev:
                combs.append(e)
            else:
                for a in prev:
                    combs.append(a+e)
        return combs




if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))#["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]