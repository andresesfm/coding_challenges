
# https://atcoder.jp/contests/dp/tasks/dp_c 

# Days
N = 3
points=[
[10, 40, 70],
[20, 50, 80],
[30, 60, 90]
]

def max_points():
  DP=[[0]*N for i in range(3)]
  for d in range(N):#days
    if d ==0:
      for a in range(3):
        DP[d][a] = points[d][a]
        continue
    for a in range(3):#activities
      for b in range(3):#activities
        if a != b:
          DP[d][b]=max(DP[d][b],DP[d-1][a]+points[d][b])
  print(DP)
  return DP[N-1][2]

print(max_points())