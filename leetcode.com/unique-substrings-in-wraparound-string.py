class NaiveSolution:
    def __init__(self):
        super().__init__()
        self.memo = {}
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        if n == 0:
            return 0
        if n == 1:
            if p[0] not in self.memo:
                self.memo[p[0]]=1
                return 1
            else:
                return 0
        
        if p in self.memo:
            return self.memo[p]
        count = 0
        if n ==2:
            if p[0] not in self.memo:
                count +=1
                self.memo[p[0]]=1
            if p[1] not in self.memo:
                count +=1
                self.memo[p[1]] =1
            if self.isSub(p) and p not in self.memo:
                count +=1
            
            self.memo[p] = count
            return count
        
        if self.isSub(p):
            count +=1
        
        count += self.findSubstringInWraproundString(p[:-1]) 
        
        for i in range(1,n):
            sub = p[i:n]
            print(sub)
            if sub not in self.memo:
                count += self.findSubstringInWraproundString(sub)
        #print(self.memo)
        self.memo[p] = count
        return count
    
    def isSub(self,p: str)-> bool:
        curr = ''
        for i in range(1,len(p)):
            if p[i] == 'a' and p[i-1] =='z':
                continue
            elif ord(p[i]) != ord(p[i-1])+1:
                return False
        return True 

class Solution:
    def __init__(self):
        super().__init__()
        self.memo = {}
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        if n == 0:
            return 0
        DP = {i:0 for i in "abcdefghijklmnopqrstuvwxyz" }
        # DP[i] is the max len of a substring ending in i
        DP[p[0]] = 1
        res = 1
        count = 1
        for i in range(1,n):
            count = (count +1) if self.isSub(p[i-1:i+1]) else 1
            if count> DP[p[i]]: # not counted
                res += count - DP[p[i]]
                DP[p[i]] = count
            print(DP)
        return res
    
    def isSub(self,p: str)-> bool:
        curr = ''
        for i in range(1,len(p)):
            if p[i] == 'a' and p[i-1] =='z':
                continue
            elif ord(p[i]) != ord(p[i-1])+1:
                return False
        return True 

if __name__ == "__main__":
    s = Solution()
    print(s.findSubstringInWraproundString("a"))#1
    s = Solution()
    print(s.findSubstringInWraproundString("cac"))#2
    s = Solution()
    print(s.findSubstringInWraproundString("zab"))#6
    s = Solution()
    print(s.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabzcd"))
    #print(s.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghij"))
    #print(s.findSubstringInWraproundString("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))