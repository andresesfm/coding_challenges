
## if it was only 2 and 3 then we could expand as follows:
## DP[0][0] =1 , DP[0][1] = 2 , DP[1][0] = 3
## ---
## 1  2  4  8
##    3  6  12 24
##       9  18 36 72
## 27 54 108 216
## ----
## DP[0] = [1]
## DP[1] = [2,3]
## DP[2] = [2,6,6,3]
## DP[3] = [4,12,12,6,6,18,18,9]
## ---
## 1  2  4  8 16 32 64 128
## 3  6  12 24 48 96 202
## 9  18 36 72 144 
## 27 54 108 216
## 81 160

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        DP = [1]
        i2 = 0
        i3 = 0
        i5 = 0
        while len(DP)<n:
            next2 = DP[i2]*2
            next3 = DP[i3]*3
            next5 = DP[i5]*5
            next = min(next2,next3,next5)
            if next == next2:
                i2+=1
            if next == next3:
                i3+=1
            if next == next5:
                i5+=1
            DP.append(next) 
        print(DP)
        return DP[n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber(10))  # 12
