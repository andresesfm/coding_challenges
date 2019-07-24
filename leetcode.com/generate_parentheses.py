from typing import List
#Does not work :(
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        
        for i in range(1,n):
            r = []
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-i)
            if not left:
                for f in right:
                    r.append('-'+f+'-')
            if not right:
                for f in left:
                    r.append('+'+f+'+')

            for e in left:
                for f in right:
                    r.append('('+e+')' + ''+f+'')
                    r.append(''+e+'' + '('+f+')')
            l = l+r
        return l

s = Solution()

l = s.generateParenthesis(3)
print(l)