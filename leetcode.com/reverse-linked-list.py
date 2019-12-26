from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        front = self.helper(head.next,head)
        head.next = None
        return front
    
    def helper(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return tail
        if not head.next:
            head.next = tail
            return head
        nt = ListNode(head.val)
        nt.next = tail
        
        rest =  self.helper(head.next,nt)
        return rest
        
    
#Print matrix
def printm(M):
    for e in M:
        print(e)

#Linked Lists:



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
    printList(s.reverseList(buildList([1,2,3,4,5])))
    # print(s.reverseList())
    # print(s.reverseList())