"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        q = collections.deque()
        digits = {'-','0','1','2','3','4','5','6','7','8','9'}
        i = 0
        n = len(s)
        while i < n:
            e = s[i]
            if e == '[':
                q.append(e)
            elif e == ',':    #no-op
                pass
            elif e in digits:
                j = i
                while j < n and s[j] in digits:
                    j+=1
                q.append(int(s[i:j]))
                i = j
            elif e == ']':
                ni = NestedInteger()
                p = q.pop()
                while not(isinstance(p,str) and p == '['):
                    if isinstance(p,int):
                        if ni.getInteger() == None and ni.getList() == None:
                            nl.setInteger(p)
                        else:
                            if ni.getList() == None:
                                ni.add(p)
                            elif ni.getInteger() == None:
                                ni.getList().insert(0,p)
                            else:
                                ni2 = NestedInteger()
                                ni2.add(p)
                                ni2.add(ni.getInteger())
                                ni = ni2
                    else:
                        if ni.getInteger() == None
                        
                    
                    p = q.pop()
            i+=1