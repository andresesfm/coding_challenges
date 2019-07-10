import random 
"""
Shuffling an array of integers
"""
def shuffle(a):
    b = [random.randint(0,len(a)) for i in range(len(a)//2)]
    for i,e in enumerate(b):
        a[i],a[e] = a[e],a[i]
    return a
print(shuffle([1,2,3,4,5,6,7]))