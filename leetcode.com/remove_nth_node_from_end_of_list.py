# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#Not working
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        bs = 0
        nthp = curr = head
        while True:
            if not curr:
                break
            
            if bs >= n+1:
                nthp = nthp.next
            bs+=1
            curr = curr.next
        if n == 1 and bs != 2:
            return None
        #nthp prev to nth
        if nthp and nthp.next:
            if not nthp.next.next and n>1:
                head = head.next
            else:
                nthp.next = nthp.next.next
        # if not nthp.next:
        #    head = head.next
        return head

s = Solution()
head = l = ListNode(1)
l.next = ListNode(2)
# l = l.next
# l.next = ListNode(3)
# l = l.next
# l.next = ListNode(4)
# l = l.next
# l.next = ListNode(5)

n = s.removeNthFromEnd(head,1)
while n:
    print(n.val ,'->')
    n = n.next