class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 1
        
        DP = [0 for i in range(n)]
        if s[n-1] =='0':
            DP[n-1]= 0
            if n == 1:
                return 0
        else:
            DP[n-1] = 1
        if n == 1: 
            return 1
        if int(s[n-2:n])<10:
            DP[n-2] = 0
        elif int(s[n-2:n]) >26 :
            DP[n-2] = DP[n-1]
        else:
            DP[n-2] = DP[n-1]+1
        
        for i in range(n-3,-1,-1):
            if s[i]=='0':
                DP[i] = 0
            else:
                DP[i] =  DP[i+1]
                if int(s[i:i+2]) >=10 and int(s[i:i+2]) <27:
                    DP[i] +=  DP[i+2]
        print(DP)
        return DP[0]



if __name__ == "__main__":
    s = Solution()
    r = s.numDecodings('110')
    print(r)
    assert r == 1
    r = s.numDecodings('101')
    print(r)
    assert r == 1
    r = s.numDecodings('100')
    print(r)
    assert r == 0
    r = s.numDecodings('27')
    print(r)
    assert r == 1
    r = s.numDecodings('01')
    print(r)
    assert r == 0
    r = s.numDecodings('10')
    print(r)
    assert r == 1
    r = s.numDecodings('12')
    print(r)
    assert r == 2
    r = s.numDecodings('226')
    print(r)
    assert r == 3
    