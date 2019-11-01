#https://atcoder.jp/contests/dp/tasks/dp_a

#number of stones   
N = 4
hs =[10, 30, 40, 20]
expected_output = 30

INF = 10e9+5

def min_tot_cost():
  DP =[INF]*N
  DP[0] = 0
  for i in range(N):
    for j in [i-1,i-2]:
      if j>=0:
        DP[i] = min(DP[i],DP[j]+abs(hs[i]-hs[j]))
  print(DP)
  return DP[N-1]

m = min_tot_cost()
print(m)
assert expected_output == m



N = 2
hs =[10, 10]
expected_output = 0

m = min_tot_cost()
print(m)
assert expected_output == m


N = 6
hs =[30, 10, 60, 10, 60, 50]
expected_output = 40

m = min_tot_cost()
print(m)
assert expected_output == m

