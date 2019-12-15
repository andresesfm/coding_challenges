from typing import List


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