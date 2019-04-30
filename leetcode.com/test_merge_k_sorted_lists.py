from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = str(self.val)
        if self.next:
            s = s + '->' + str(self.next)
        return s

    def __repr__(self):
        return self.__str__()

def mergeKLists(lists: List[ListNode]) -> ListNode:
    #current indices
    head = None
    tail = None
    while True:
        minNode = None
        maxI = None
        for i,l in enumerate(lists):
            if l:
                if minNode:
                    if minNode.val > l.val:
                        minNode = l
                        maxI = i
                else:
                    minNode = l
                    maxI = i
        if tail and minNode:
            tail.next = ListNode(minNode.val)
            tail = tail.next
        elif minNode:
            head = ListNode(minNode.val)
            tail = head
        if maxI != None:
            lists[maxI] = lists[maxI].next
        
        if minNode == None:
            break
    return head


l11 = ListNode(1)
l11.next = ListNode(3)
l11.next.next = ListNode(5)
l22 = ListNode(2)
l22.next = ListNode(4)
l22.next.next = ListNode(6)
l = [l11,l22]
print(l)
m = mergeKLists(l)
print(m)