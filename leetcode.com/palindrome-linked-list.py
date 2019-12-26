from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        if not head.next.next.next:
            return head.val == head.next.next.val
        root = head
        cnt = 0
        while root:
            cnt+=1
            root = root.next
        root = head
        i =0
        half = cnt //2
        if cnt %2 ==1:
            half += 1
        while root and i < half:
            i+=1
            root = root.next
        nr = ListNode(root.val)
        revtail =  self.reverse(root.next,nr)
        i = 0
        h2 = head

        while h2 and revtail and i < cnt//2:
            if h2.val != revtail.val:
                return False
            h2 = h2.next
            revtail = revtail.next
        return True

    def reverse(self, head: ListNode, tail: ListNode) -> ListNode:
        if not head:
            return tail
        if not head.next:
            head.next = tail
            return head
        nt = ListNode(head.val)
        nt.next = tail
        
        rest =  self.reverse(head.next,nt)
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
    print(s.isPalindrome(buildList([1,2])))#false
    print(s.isPalindrome(buildList([1,2,2,1])))#true
    print(s.isPalindrome(buildList([1,0,0])))#false
    print(s.isPalindrome(buildList([1,1,2,1])))#false