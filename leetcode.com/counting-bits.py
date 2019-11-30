from typing import List

## 0    0
## 1    1
## 10   1
## 11   2
## 100  1
## 101  2
## 110  2
## 111  3
## 1000 1
## 1001 2
## 1010 2
## 1100 2
## 1101 3
## 1110 3
## 1111 4
## 10000 1
class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        res = [len([ones for ones in bin((i &(i-1))+1)[2:] if ones =='1']) for i in range(1,num+1)]
        return [0] + res

if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))#[0,1,1]
    print(s.countBits(5))#[0,1,1,2,1,2]