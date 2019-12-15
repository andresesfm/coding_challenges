from typing import List
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        INF = 1e9+5
        n = len(s)
        if len(t)>n:
            return ""
        c = {}
        valid = set(t)
        l = 0
        r = 0
        res = None
        req = Counter(t)
        cnt = 0
        def validate():
            return all([e in c and req[e]<= c[e] for e in req])
        
        while l<n:
            if validate(): #includes all characters
                if res == None:   
                    res = s[l:r]
                else:
                    if len(res) > len(s[l:r]):
                        res = s[l:r]
                if s[l] in valid and s[l] in c:
                    if c[s[l]] <= 1:
                        c.pop(s[l])
                    else:
                        c[s[l]] -= 1
                    if s[l] not in c or req[s[l]]> c[s[l]]:
                        cnt-=1
                l+=1
            else:
                if r<n:
                    if s[r] in valid:
                        if not s[r] in c:
                            c[s[r]] = 1
                        else:
                            c[s[r]] += 1
                    r+=1
                else:
                    l+=1
            # print(l,r)
            # print(res)
            # print(s[l:r])
        return res if res else ''
                    

                
def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow( "ADOBECODEBANC", "ABC"))#BANC
    print(s.minWindow("aa","aa"))#aa
    print(s.minWindow("cabwefgewcwaefgcf","cae"))#cwae
    print(s.minWindow("bba","ab"))#ba