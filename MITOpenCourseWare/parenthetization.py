# Implement Parenthetization using technique described here: https://www.youtube.com/watch?v=ocZMDMZwhCY

# 1 Define subproblems: Optimal multiplication of product of A_i ... A_j 
#   Number of subproblems is n^2
# 2 Guess the last multiplication. Meaning indices k,i,j  such that  i<=k<=j-1 , i<=j in 0... n-1

# 3 Recurse and memoize 
# DP(i,j) = min(
#    DP(i,k) + DP(k-j) + cost((A_i:k)(A_k:j)
#      
# ) for k in range(i+1-j)
# Time / subproblem is O(n)
# 4 Time = O(n^3) 
# Topological Order: Small to large
def paren(mats):
    return parenDP(mats,0,len(mats)-1)

memo ={}

def parenDP(mats, i,j):
    if f'{i},{j}' in memo:
        return memo[f'{i},{j}']
    if j-i<1:
        memo[f'{i},{j}']= i
        return i
    if j-i < 2:
        memo[f'{i},{j}']= i+1
        return i+1
    min_cost = 100000000
    min_k = -1
    for k in range(i+1,j):
        c = parenDP(mats,i,k) + parenDP(mats,k,j) + cost(mats,i,k,j)
        if c < min_cost:
            min_cost = c
            min_k = k
    memo[f'{i},{j}']= min_k
    return min_k
def cost(mats ,i,k,j):
    return mats[i][0] * mats[k][1] + mats[k][0] * mats[j][1]

t = [(1,5),(5,4),(4,1),(1,20)]
print(paren(t))
print(memo)

t1 = [(2,3),(3,6),(6,4),(4,5)]
## Bottom up:
memoBU = []
def parenBU(mats):
    l = len(mats)
    global memoBU
    memoBU = [[0 for col in range(l)] for row in range(l)]
    for k in range(1,l):
        i = 0 
        j = k
        while(i<l and j < l):
            v1 = memoBU[i-1][j]
            v2 = memoBU[i][j-1]
            c = v1 + v2 + cost(mats,i,k,j)
            memoBU[i][j] = c
            i+=1
            j+=1
    return memoBU[0][l-1]

print(parenBU(t1))

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
for row in memoBU]))