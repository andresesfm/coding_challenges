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

def parenDP(mats, i,j):
    if j-i<1:
        return i
    if j-i == 2:
        return i+1
    min_cost = 100000000
    min_k = -1
    for k in range(i+1,j):
        c = parenDP(mats,i,k) + parenDP(mats,k,j) + cost(mats,i,k,j)
        if c < min_cost:
            min_cost = c
            min_k = k
    return min_k
def cost(mats ,i,k,j):
    return mats[i][0] * mats[k][1] + mats[k][0] * mats[j][1]

t = [(1,5),(5,4),(4,1)]
print(paren(t))