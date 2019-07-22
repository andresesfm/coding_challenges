# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        while True:
            if l1:
                n1 = l1.val
            else:
                n1 = None
            if l2:
                n2 = l2.val
            else:
                n2 = None
            
            if n1 == None and n2 == None:
                break
            elif n1 != None and n2 != None:
                if n1 <= n2:
                    node = ListNode(n1)
                    l1 = l1.next
                else:
                    node = ListNode(n2)
                    l2 = l2.next
            elif n1 != None:
                node = ListNode(n1)
                l1 = l1.next
            elif n2 != None:
                node = ListNode(n2)
                l2 = l2.next
            
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
        return head

s = Solution()
l1 = l1t = ListNode(1)
l1t.next = ListNode(2)
l1t = l1t.next
l1t.next = ListNode(4)
l1t = l1t.next

l2 = l2t = ListNode(1)
l2t.next = ListNode(3)
l2t = l2t.next
l2t.next = ListNode(4)
l2t = l2t.next

l = s.mergeTwoLists(l1,l2)
while l:
    print(l.val, '->')
    l = l.next