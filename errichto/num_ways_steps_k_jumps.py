# https://www.youtube.com/watch?v=YBSt1jYwVfU

#ways to climb n steps with at most K jumps
def waysToClimbKsteps(n,k):
  print('hello')
  F = [[0]*k for i in range(n)]
  F[0][0] = 0
  F[0][1] = 1
  F[1][0] = 0
  F[1][1] = 1

  for i in range(1,n):
    for j in range(1,k):
      F[i][j] =F[i-1][j-1] + F[i-2][j-1] 
  print(F)
  return sum(F[n-1][j] for j in range(0,k) )
  


print(waysToClimbKsteps(5,5))