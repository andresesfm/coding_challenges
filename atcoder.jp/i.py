# https://atcoder.jp/contests/dp/tasks/dp_i
import sys

line_count=0
for line in sys.stdin:
  if line_count==0:
    N = int(line)
  else:
    Ps=[float(i) for i in line.split(' ')]
  line_count+=1

print(Ps)
DP=[0]*(N+1)
DP[0]=1
for coin in range(N):
  for i in range(coin+1,-1,-1):
    if i ==0:
      heads = 0
    else:
      heads = DP[i-1]*Ps[i-1]

    DP[i] = heads + DP[i]*(1-Ps[i-1])
  
answer = 0.0
for heads in range(N):
  tails = N-heads
  if heads>tails:
    answer+=DP[heads]
  
print(DP)
print (answer)

