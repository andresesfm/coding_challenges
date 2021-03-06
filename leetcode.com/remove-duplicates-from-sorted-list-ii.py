from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import Counter
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        root = head
        cnt = Counter()
        while root:
            cnt[root.val] +=1
            root = root.next
        root = head
        root2 = root
        while root:
            if cnt[root.val]>1 and root == root2:
                    root2 = root2.next
                    root  = root.next
            elif root.next and cnt[root.next.val]>1:
                    root.next = root.next.next
            else:
                root  = root.next
        return root2
    

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