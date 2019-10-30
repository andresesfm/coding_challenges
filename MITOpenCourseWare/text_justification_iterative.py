# List of lenghts of the words as they appear in the text
words = [2, 4, 1, 5, 9, 1, 1]
words_len =len(words)
# desired line length
line_lenght = 10
MAX = 10000000000


def badness(i, j):
    bad = 0
    for k in range(i, j+1):
        bad += words[k]
    if(line_lenght<bad):
        return MAX
    else:
        return abs(line_lenght-bad)# pow(line_lenght-bad, 3)


def justify():
  for l in range(words_len-1,0,-1):
    justify_dp(l)
  return DP[0]

DP =[MAX]*(words_len)
DP[words_len-1]=0
parent_pointer=[MAX]*(words_len)
def justify_dp(k):
    nlbc = MAX# next line break cost
    index = None
    for j in range( k, words_len):
        nl = badness(k,j) + DP[j]
        if nl < nlbc:
            index = j
            nlbc = nl
    if index:
        DP[k-1] = nlbc
        parent_pointer[k-1]= index
        print(DP)
    return(nlbc)


print(justify())
#print(DP)
# while(True):
print(parent_pointer)

