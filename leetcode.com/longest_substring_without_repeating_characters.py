import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        i = 0
        j = 0
        m = 0
        while j < len(s):
            if s[j] in chars:
                m = max(m, j-i)
                chars.remove(s[i])
                i+=1
                continue
            else:
                chars.add(s[j])
            j+=1
        return max(m,j-i)

class TestSolution(unittest.TestCase):
    def test_provided(self):
        s = Solution()
        self.assertEquals(3,s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEquals(0,s.lengthOfLongestSubstring(""))
        self.assertEquals(1,s.lengthOfLongestSubstring(" "))

if __name__ == "__main__":
    unittest.main()
    