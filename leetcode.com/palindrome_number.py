import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        numDigits = math.floor(math.log(x,10))+1
        print("digits",numDigits)
        for i in range(numDigits):
            firstDigit = self.getDigit(x,i)
            print("first", firstDigit)
            lastDigit = self.getDigit(x,numDigits-i-1)
            print("last",lastDigit)
            if firstDigit == lastDigit:
                continue
            return False
        return True
    
    def getDigit(self,x:int,index:int):
        return math.floor(x/math.pow(10,index)) %10

s = Solution()
print(s.isPalindrome(121))