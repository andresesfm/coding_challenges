import unittest

#From leetcode: https://leetcode.com/problems/minimum-window-substring/description/
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

def min_window_subs(s,t):
    bag = set()
    i =0
    j =0
    l = len(s)
    while True:
        if j< l:
            if s[j] in t:
                if s[j] not in bag:
                    bag.add(s[j])
                    if len(bag) == len(t):
                        break
                else:
                    if s[i]==s[j]:
                        i+=1
            j+=1
            print(s[i:j])
        else:
            break
    if i<=j:
        return s[i:j]
    return ""


#This didn't work
def min_window_subs_first_attempt(s,t):
    ranges = {}
    for i, e in enumerate(s):
        if e in t:
            if e not in ranges:
                #Found first entry
                ranges[e] = (i,None)
            else:
                #Update max range
                ranges[e] = (ranges[e][0],i)

    start = 0
    end = len(s)+1
    for e in ranges:
        start = max(start,ranges[e][0])
        if not ranges[e][1]:
            return "" #Element not found
        end = min(end, ranges[e][1])
        if end<start:
            return ""
    return s[start:end]

class MinWinTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual("", min_window_subs("","A"))

    def test_provided_example(self):
        self.assertEqual("BANC", min_window_subs("ADOBECODEBANC","ABC"))