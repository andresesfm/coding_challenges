from typing import List

class NotWorkingRecursiveSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.mergeR(intervals)
    def mergeR(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or not intervals[0]:
            return []
        if len(intervals)==1:
            return intervals
        if len(intervals)==2:
            return self.helper(intervals[0],intervals[1])
        else:
            return self.mergeR([intervals[0]] + self.mergeR(intervals[1:]))
        
    def helper(self,i1:List[int], i2:List[int])-> List[List[int]]:
        if (i1[0]<= i2[1] and i1[0] >= i2[0]) or (i1[1]>= i2[0] and i1[1] <= i2[1]) or (i1[0]<=i2[0] and i1[1]>=i2[1]) or (i2[0]<=i1[0] and i2[1]>=i1[1]):
            return[[min(i1[0],i2[0]),max(i1[1],i2[1])]]
        else:
            return[i1,i2]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = []
        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1],i[1])
        return merged


def printm(M):
    for e in M:
        print(e)

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))#[[1,6],[8,10],[15,18]]
    print(s.merge([[1,4],[4,5]]))#[[1,5]]
    print(s.merge([[1,4],[0,5]]))#[[0,5]]
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))#[[1,10]]