# https://www.youtube.com/watch?v=YBSt1jYwVfU

def waysToClimb(n):
  F=[0]*n
  F[0]=0
  F[1]=1
  for i in range (2,n):
    F[i] = F[i-1]+F[i-2]
  print(F)
  return F[n-1]

print(waysToClimb(10))