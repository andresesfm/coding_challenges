import sys

modulo = int(1e9+7)

line_count=0
for line in sys.stdin:
  if line_count==0:
    H,W = [int(i) for i in line.split()]
    S = [[] for i in range(H)]
    DP =[[0]*W for i in range(H)]
  else:
    S[line_count-1] = list(filter(lambda x: x!= '\n',list(line)))
  line_count+=1
print(S)
print(modulo)

def is_wall(c):
  return c == '#'
def add_mod(i,j,i2,j2):
  DP[i][j]+= DP[i2][j2]
  if DP[i][j]> modulo:
    DP[i][j] -= modulo 
DP[0][0]=1
for i in range(H):
  for j in range(W):  
    if not is_wall(S[i][j]):
      top = 0
      left = 0
      if i>0 and not is_wall(S[i-1][j]):
          add_mod(i,j,i-1,j)
      if j>0 and not is_wall(S[i][j-1]):
          add_mod(i,j,i,j-1)
      
      
print(DP)
print(DP[H-1][W-1])
