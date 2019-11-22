from typing import List
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def print(self):
      s = ""
      s+=str(self.val)
      if self.left:
        s+=' '+self.left.print()
      else:
        s+=' /'
      if self.right:
        s+=' ' +self.right.print()
      else:
        s+=' \\'
      return s

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generateTreesH([i+1 for i in range(n)])
    def generateTreesH(self,arr:List[int]) -> List[TreeNode]:
        n = len(arr)
        if n == 0:
            return []
        elif n == 1:
            return[TreeNode(arr[0])]
        elif n == 2:
            t1 = TreeNode(arr[0]) ## left of n
            t1.right = TreeNode(arr[1]) 
            t2 = TreeNode(arr[1])
            t2.left = TreeNode(arr[0])
            return [t1, t2]
        else:
            treeList = []
            for i in range(n):
                root = TreeNode(arr[i])
                if i>0:
                    left = self.generateTreesH(arr[:i])
                else:
                    left = []
                if i+1 < n:
                    right = self.generateTreesH(arr[i+1:])
                else:
                    right = []

                if not left:
                    for r in right:
                        nr = copy.copy(root)
                        nr.right = copy.deepcopy(r)
                        treeList.append(nr) 
                elif not right:
                    for l in left:
                        nr = copy.copy(root)
                        nr.left = copy.deepcopy(l)
                        treeList.append(nr)
                else:
                    for l in left:
                        for r in right:
                            nr = copy.copy(root)
                            nr.left = copy.deepcopy(l)
                            nr.right = copy.deepcopy(r)
                            treeList.append(nr)
            return treeList
          

          


if __name__ == "__main__":
    s = Solution()
    for t in s.generateTrees(3):
      print(t.print())