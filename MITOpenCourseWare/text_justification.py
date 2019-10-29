# List of lenghts of the words as they appear in the text
words = [2, 4, 1]#, 5, 9, 1, 1]
# desired line length
line_lenght = 10
MAX = 10000000000


def badness(i, j):
    bad = 0
    for k in range(i, j):
        bad += words[k]
    if(line_lenght<bad):
        return MAX*3
    else:
        return pow(line_lenght-bad, 3)


#print( badness(0,6))
# print(badness(0,1))
# print(badness(0,4))
parent_pointer = {}

memo = {}

def justify(i):
    if i >= len(words):
        return 0
    if i in memo:
        return memo[i]
    nlbc = MAX# next line break cost
    index = None
    for j in range(i+1, len(words)+1):
        nl = badness(i, j) + justify(j)
        if nl < nlbc:
            index = j
            nlbc = nl
    
    #print(next_line)
    if index:
        parent_pointer[i] = index 
        print(index)
    memo[i] = nlbc
    print(memo)
    return(nlbc)


print(justify(0))
# while(True):
#print(parent_pointer)
