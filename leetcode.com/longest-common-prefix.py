from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) ==0:
            return ""
        lastIndex = 0
        while True:
            allMatch = -1
            c = None
            for i in range(len(strs)):
                if len(strs[i]) <=lastIndex:
                    break
                if not c:
                    c = strs[i][lastIndex]
                else:
                    if strs[i][lastIndex]!=c: 
                        break
                allMatch = i
            if allMatch >=0 and allMatch ==len(strs)-1:
                lastIndex +=1
            else:
                break
        if strs[0]:
            return strs[0][:lastIndex]
        else:
            return "" 

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))#fl
    print(s.longestCommonPrefix(["dog","racecar","car"]))#""
    print(s.longestCommonPrefix([""]))#""
    print(s.longestCommonPrefix(["a"]))#"a"


