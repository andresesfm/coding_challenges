from typing import List
"""
From: https://www.youtube.com/watch?v=4UWDyJq8jZg
"""


class Person:
    def __init__(self, b,d):
        self.b = b
        self.d = d

def get_year(persons: List[Person]) -> int:
    years = [0 for i in range(2019)]
    for p in persons:
        years[p.b] +=1
        years[p.d] -=1

    mYear = 0
    mCount =0
    count = 0
    for y, c in enumerate(years):
        count += c
        if count > mCount:
            mCount = count
            mYear = y
    return mYear

p1 = [Person(1800,1820),Person(1819,1834)]

print(get_year(p1))