from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

INF = 1e21+5
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        try:
            self.minMax(root)
        except:
            print('failed')
            return False
        return True
    
    def minMax(self,root:TreeNode):
        if not root:
            return (INF,-INF)
        if not root.left and not root.right:
            return (root.val,root.val)
        mml = self.minMax(root.left)
        mmr = self.minMax(root.right)
        if mml[1]>= root.val or mmr[0]<=root.val:
            raise Error("Invalid")
        return (min(root.val,mml[0]), max(mmr[1],root.val))
        
#Print matrix
def printm(M):
    for e in M:
        print(e)

#Linked Lists:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def buildList(a):
    tail = None
    for e in reversed(a):
        if tail == None:
            tail  = ListNode(e)
        else:
            n = ListNode(e)
            n.next = tail
            tail = n
    #printList(tail)
    return tail

def printList(node: ListNode):
    while node:
        print(node.val,'->')
        node = node.next

if __name__ == "__main__":
    s = Solution()
    print(s.())
    print(s.())
    print(s.())