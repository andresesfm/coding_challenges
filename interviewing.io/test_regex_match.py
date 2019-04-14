import unittest
# Solution to https://www.youtube.com/watch?v=tj_sBZw9nS0&t=1240s Google Interview
def matches(s:str,r:str) -> bool:
    # if s and r are empty then true
    if not s and not r:
        return True
    # if r is empty means we ran out of things to check but s still continues, return false
    if not r and s:
        return False
    # if r is empty means we ran out of string before completing the  matching return false
    if not s:
        if len(r) >1 and r[1] == '*':#and the rest of r does not contain anything but .*
            return True
        return False
    # if first element of r is '.' test next elements
    # if first element of s matches first element of r then test following elements
    if r[0] == '.' or r[0] == s[0]:
        # if second element of s is * then test current element against the next element of s
        if len(r) > 1 and r[1] =='*':
            return matches(s[1:],r)
        
        return matches(s[1:],r[1:]) 
    elif len(r) > 2 and r[1] =='*':
        return matches(s,r[2:])
    # else means we found a mismatch
    else:
        return False  

    pass


class TestMatches(unittest.TestCase):
    def testEmpty(self):
        self.assertTrue(matches('',''))

    def testProvided(self):
        self.assertTrue(matches('a','a'))
        self.assertTrue(matches('ab','ab'))
        self.assertTrue(matches('aaa','a*'))
        self.assertTrue(matches('abc','a*bc'))
        self.assertFalse(matches('abab','abb*a'))
        self.assertTrue(matches('aasdf','.*'))
        self.assertTrue(matches('aasdf','.*.*'))
