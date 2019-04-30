import unittest

def matches(s: str, r: str) -> bool:
    if not s and not r:
        return True
    if not r:
        return False
    if not s:
        return (len(r)>=2 and r[1] =='*')

    if s[0] == r[0]:
        if len(r)>=2 and r[1] == '*':
            return matches(s[1:],r)
        else:
            return matches(s[1:],r[1:])
    if r[0] == '.':
        if len(r)>=2 and r[1] == '*':
            return matches(s[1:], r)
        else:
            return matches(s[1:],r[1:])
    
    if len(r)>=3 and r[1] == '*':
        return matches(s[2:],r)
    return False

print(matches('a','a'))
print(matches('aba','a.a'))
print(matches('abb','ab*'))
print(matches('abb','aa*'))
print(matches('abb','a*'))
print(matches('aaa','a*'))
print(matches('abc','.*'))