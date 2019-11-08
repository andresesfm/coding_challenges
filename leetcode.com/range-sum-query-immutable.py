import sys
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        if n ==0:
          return
        DP = [0 for i in range(n)]
        DP[0] = nums[0]
        for i in range(n-1):
          DP[i+1] = DP[i]+nums[i+1]
        #print(DP)
        self.DP = DP

    def sumRange(self, i: int, j: int) -> int:
      return self.DP[j]- self.DP[i-1]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

for line in sys.stdin:
  nums = [int(i) for i in line.split(',')]
  print(nums)

if __name__ == "__main__":
    s=NumArray(nums)
    print(s.DP)
    assert  1 == s.sumRange(0,2)
    assert -1 == s.sumRange(2,5)
    assert -3 == s.sumRange(0,5)
