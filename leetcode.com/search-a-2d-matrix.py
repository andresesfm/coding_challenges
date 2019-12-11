from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = n
        mid = l + (r-l)//2
        if matrix[n-1][0]<target:
            mid = n-1
        else:
            while l<=r:
                print(l,mid,r)
                e = matrix[mid][0]
                if e == target:
                    break
                elif e <target:
                    l = mid
                else:
                    r = mid
                mid = l + (r-l)//2
                
                if l == mid or r == mid:
                    break
        print(mid)
        row = mid
        l =0
        r = m
        mid = l + (r-l)//2
        while l<=r:
            print(l,mid,r)
            e = matrix[row][mid]
            if e == target:
                return True
            elif e <target:
                l = mid
            else:
                r = mid
            mid = l + (r-l)//2
            
            if l == mid or r == mid:
                break
        return matrix[row][mid] == target


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ],target = 3))
    print(s.searchMatrix(matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ],target = 13))
    print(s.searchMatrix([[1,1]],2))
    print(s.searchMatrix([[1,3]],1))