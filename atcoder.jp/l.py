import sys

line_count =0
for line in sys.stdin:
  if line_count==0:
    N = int(line)
  else:
    A = [int(i) for i in line.split(' ')]
  line_count+=1

print(N)
print(A)

DP= [[0]*N]*N

# DP[l][r] is the score given Taro took i and Jiro took jth element
for l in range(N-1,-1,-1):
  for r in range(l,N):
    if r == l:
      DP[r][l] = A[l]
    else:
      DP[l][r] = max(A[l]-DP[l-1][r], A[r]- DP[l][r-1])


print(DP)
print(DP[0][N-1])