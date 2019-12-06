# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        last = 0
        nh = head
        while nh:
            nh = nh.next
            last +=1
        count = 0
        rh = head
        if last-n ==0:
            return head.next
        while count < last-n-1:
            rh = rh.next
            count +=1
        if rh:
            if rh.next:
                rh.next = rh.next.next
            else:
                rh.next = None
        return head

s = Solution()
head = l = ListNode(1)
l.next = ListNode(2)
l = l.next
l.next = ListNode(3)
l = l.next
l.next = ListNode(4)
l = l.next
l.next = ListNode(5)

n = s.removeNthFromEnd(head,1)
while n:
    print(n.val ,'->')
    n = n.next