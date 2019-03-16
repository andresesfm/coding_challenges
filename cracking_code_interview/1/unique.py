import unittest

def unique(s):
    return len(s) == len(set(s))

def unique_no_ds(s):
    for i in range(len(s)):
        if any(s[i]==s[j] for j in range(i+1,len(s))):
             return False
    
    return True

def unique_with_alphabet(s):
    chars = [False for _ in range(256)]
    for e in s:
        if chars[ord(e)]:
            return False
        else:
            chars[ord(e)]= True
    return True


class UniqueTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(unique(""))
        self.assertTrue(unique_no_ds(""))
        self.assertTrue(unique_with_alphabet(""))

    def test_dup(self):
        self.assertFalse(unique("AA"))
        self.assertFalse(unique_no_ds("AA"))
        self.assertFalse(unique_with_alphabet("AA"))
    
    def test_begining_end(self):
        self.assertFalse(unique("abca"))
        self.assertFalse(unique_no_ds("abca"))
        self.assertFalse(unique_with_alphabet("abca"))

if __name__ == '__main__':
    unittest.main()