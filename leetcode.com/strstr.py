"""
Solution to : https://leetcode.com/problems/implement-strstr/
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle)> len(haystack):
            return -1
        match = True
        mh = 0
        while mh <len(haystack):
            mn = 0
            lmh = mh
            while lmh < len(haystack) and mn < len(needle):
                if haystack[lmh] != needle[mn]:
                    break
                lmh +=1
                mn +=1
            if mn == len(needle):
                return mh
            if len(needle)> len(haystack)-mh:
                break
            mh += 1
        return -1
                
s = Solution()
r = s.strStr("mississippi", "mississippi")
print(r)