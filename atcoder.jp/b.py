# https://atcoder.jp/contests/dp/tasks/dp_b

# number of stones
N = 5
# max jump height
K =3
# Stone heights
hs = [10, 30, 40, 50, 20]

expected_result=30

INF = 10e9+5

def min_cost():
  DP=[INF]*N
  DP[0] = 0
  for i in range(N):
    for j in range(i+1,i+K+1):
      if j<N:
        DP[j] = min(DP[j], DP[i]+abs(hs[i]-hs[j]))
  print(DP)
  return DP[N-1]

m = min_cost()
print(m)
assert m == expected_result