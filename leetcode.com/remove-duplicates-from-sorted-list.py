from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head.next = self.firstDifferent(head.next,head.val)
        return head
    
    def firstDifferent(self,head:ListNode, val):
        root = head
        while root:
            if root.val == val:
                root = root.next
            else:
                break
        if root:
            root.next = self.firstDifferent(root.next,root.val)
        return root

def printm(M):
    for e in M:
        print(e)

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
    printList(s.deleteDuplicates(buildList([1,2,3,3,4,4,5])))
    # printList(s.deleteDuplicates(buildList([1,1,1,2,3])))
    # print(s.deleteDuplicates())